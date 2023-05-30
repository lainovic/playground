class Promise {
	constructor(executor) {
		this.value = undefined
		this.error = undefined
		this.isFullfilled = undefined
		this.isRejected = undefined
		this.callbacks = undefined

		const resolve = value => {
			if (this.isFullfilled || this.isRejected) {
				return;
			}
			this.value = value;
			this.isFullfilled = true;
			this.callbacks.forEach(callback => callback.onFullfilled(value));
		}

		const reject = error => {
			if (this.isFullfilled || this.isRejected) {
				return;
			}
			this.error = error;
			this.isRejected = true;
			this.callbacks.forEach(callback => callback.onRejected(error));
		}

		try {
			executor(resolve, reject);
		} catch (error) {
			reject(error);
		}
	}

	then(onFullfilled, onRejected) {
		const callback = {};
		callback.onFullfilled = typeof onFullfilled === 'function' ? onFullfilled : value => value;
		callback.onRejected = typeof onRejected === 'function' ? onRejected : error => { throw error };

		const promise = new Promise((resolve, reject) => {
			if (this.isFullfilled) {
				setTimeout(() => {
					try {
						const res = callback.onFullfilled(this.value);
						resolve(res);
					} catch (error) {
						reject(error);
					}
				}, 0);
			} else if (this.isRejected) {
				setTimeout(() => {
					try {
						const res = callback.onRejected(this.error);
						resolve(res);
					} catch (error) {
						reject(error);
					}
				}, 0);
			} else {
				this.callbacks.push(callback);
			}
		});

		return promise;
	}

	catch(onRejected) {
		return this.then(undefined, onRejected);
	}
}
