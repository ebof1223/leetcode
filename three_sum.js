var threeSum = function(nums) {

	var triplets = [];

	for (let i = 0; i < nums.length; i++) {
		let x = nums.length - 2;
		let y = nums.length - 1;
		while (y < nums.length && i < x) {
			const sum = nums[i] + nums[x] + nums[y];
			if (sum == 0) {
				triplets.push([nums[i], nums[x], nums[y]]);
				break;
			}
			else if (sum < 0) {
				y++;
			} else if (0 < sum) {
				x--;
			}
		}
	}
	return triplets;
};

console.log(threeSum([-4, -1, -1, 0, 1, 2]));
