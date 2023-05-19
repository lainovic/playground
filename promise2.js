class LyPromise {
	constructor(executor) {
		this.state = "pending"
		this.onFullfilled = undefined
		this.onRejected = undefined
		this.onSettled = undefined
		this.res = undefined
		this.err = undefined

		this.resolve = (res) => {
			if (this.state !== "pending") return
			this.state = "fullfilled"
			if (this.onFullfilled) {
				this.onFullfilled(res)
				this.state = "settled"
				if (this.onSettled) this.onSettled()
			}
			else this.res = res
		}

		this.reject = (err) => {
			if (this.state !== "pending") return
			this.state = "rejected"
			if (this.onRejected) {
				this.onRejected(err)
				this.state = "settled"
				if (this.onSettled) this.onSettled()
			}
			else this.err = err
		}

		try {
			executor(this.resolve, this.reject)
		}
		catch (e) {
			reject(e)
		}
	}

	then(onFullfilled, onRejected) {
		if (this.state == "fullfilled") {
			onFullfilled(this.res)
			if (this.onSettled) this.onSettled()
			else this.state = "settled"
		}
		else if (this.state == "rejected") {
			onRejected(this.err)
			if (this.onSettled) this.onSettled()
			else this.state = "settled"
		}
		else {
			this.onFullfilled = onFullfilled
			this.onRejected = onRejected
		}
	}

	catch(onRejected) {
		if (this.state == "rejected") {
			onRejected(this.err)
			if (this.onSettled) this.onSettled()
			else this.state = "settled"
		}
		else {
			this.onRejected = onRejected
		}
	}

	finally(onSettled) {
		if (this.state == "settled") {
			onSettled()
		}
		else {
			this.onSettled = onSettled
		}
	}
}

const promise = new LyPromise((resolve, reject) => {
	setTimeout(() => {
		resolve("done!");
	}, 1000);
});
promise.then(res => {
	console.log(res);
});

setTimeout(() => {
	promise.then(res => { console.log(res); });
}, 2000);

// function getPromise() {
// 	return new Promise((resolve, reject) => {
// 		setTimeout(() => {
// 			resolve("bam! done");
// 		}, 1000);
// 	});
// }
//
// getPromise().then(res => { console.log(res); });


