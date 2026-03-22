/**
 * Enhances all arrays such that you can call the arr.last() method on any array 
 * and it will return the last element. If there are no elements in the array, 
 * it should return -1.
 * 
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    if (this.length === 0) {
        return -1;
    }
    return this[this.length - 1];
};

/**
 * const arr = [1, 2, 3];
 * arr.last(); // 3
 */

// Test cases
if (require.main === module) {
    const arr1 = [null, {}, 3];
    console.log(`Example 1: ${arr1.last()}`); // 3

    const arr2 = [];
    console.log(`Example 2: ${arr2.last()}`); // -1
}
