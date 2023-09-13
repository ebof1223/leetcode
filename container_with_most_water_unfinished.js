//naive
const maxArea_naive = (height) => {
	let max_vol_total = 0;
	for (let i = 0; i < height.length - 1; i++) {

		let p = height.length - 1;

		while (i < p) {

			const coor_i = [i + 1, height[i]];
			const coor_p = [p + 1, height[p]];
			const delta_x = coor_p[0] - coor_i[0];
			const delta_y = Math.min(coor_i[1], coor_p[1]);
			const volume = delta_x * delta_y;

			max_vol_total = Math.max(max_vol_total, volume)
			p--;
		}
	}
	return max_vol_total;
}


//while 
//l0, r=end
//calculate x delta
//caculate y
//comp max and curr

const maxArea = (height) => {

	let max_vol_total = 0;
	let l = 0;
	let r = height.length - 1;

	while (l < r) {
		const delta_x = r - l;
		const max_height = Math.min(height[l], height[r]);
		const volume = delta_x * max_height;
		max_vol_total = Math.max(volume, max_vol_total);


		if (height[l] < height[r]) {
			l++;
		} else {
			r--;
		}

	}
	return max_vol_total;
}

console.log(maxArea([1,8,6,2,5]));









