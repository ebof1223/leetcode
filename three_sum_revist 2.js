var threeSum = function(nums) {

	nums.sort((a, b) => a - b);
	var triplets = [];

	for (let i = 0; i < nums.length; i++) {
		let left = i + 1;
		let right = nums.length - 1;
		if (i > 0 && nums[i] == nums[i - 1]) continue;

		while (left < right) {
			const sum = nums[i] + nums[left] + nums[right];

			if (sum < 0) {
				left++;
			}
			else if (0 < sum) {
				right--;
			} else {
				triplets.push([nums[i], nums[left], nums[right]]);
				while (nums[left] == nums[left + 1]) left++;
				while (nums[right] == nums[right - 1]) right--;
				left++;
				right--;

			}
		}
	}
	return triplets;
};

console.log(threeSum([-4, -1, -1, 0, 1, 2]));
