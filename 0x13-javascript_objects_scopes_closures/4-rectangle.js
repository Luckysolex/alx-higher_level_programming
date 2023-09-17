#!/usr/bin/node
module.exports = class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) { [this.width, this.heigth] = [w, h]; }
	}

	print () {
		for (let i = 0; i < this.height; i++) console.log('X'.repeat(this.width));
	}

	rotate () {
		[this.width, this.heigth] = [this.heigth, this.width];
	}

	double () {
		[this.width, this.heigth] = [this.width * 2, this.heigth * 2];
	}
};
