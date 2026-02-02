class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = (1 if not has_lower else 0) + (1 if not has_upper else 0) + (1 if not has_digit else 0)
        
        # Repeating sequences of length >= 3
        repeat_counts = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            if j - i >= 3:
                repeat_counts.append(j - i)
            i = j
            
        if n < 6:
            return max(6 - n, missing_types)
        elif n <= 20:
            replace_needed = sum(count // 3 for count in repeat_counts)
            return max(replace_needed, missing_types)
        else:
            # More than 20 characters
            delete_needed = n - 20
            
            # Prioritize deletions that reduce the number of replacements needed
            # count % 3 == 0 -> Needs 1 deletion to save 1 replacement
            # count % 3 == 1 -> Needs 2 deletions to save 1 replacement
            # count % 3 == 2 -> Needs 3 deletions to save 1 replacement
            
            # Group repeats by their modulo 3
            rem0 = 0
            rem1 = 0
            for count in repeat_counts:
                if count % 3 == 0:
                    rem0 += 1
                elif count % 3 == 1:
                    rem1 += 1
            
            # Use deletions on count % 3 == 0
            d = delete_needed
            use = min(d, rem0)
            d -= use
            replace_reduction = use
            
            # Use deletions on count % 3 == 1
            use = min(d, rem1 * 2)
            d -= use
            replace_reduction += use // 2
            
            # Use remaining deletions on count % 3 == 2 (or remaining from before)
            replace_reduction += d // 3
            
            total_replace = sum(count // 3 for count in repeat_counts)
            replace_needed = max(total_replace - replace_reduction, missing_types)
            
            return delete_needed + replace_needed
