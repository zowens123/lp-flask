const check = () => {
	if (!('serviceWorker' in navigator)) {
		throw new Error('No Service Worker support')
	}
	if (!('PushManager') in window) {
		throw new Error('No Push API support')
	}
}

//function to add a service worker
const registerServiceWorker = async () => {
	const swRegistration = await
	navigator.serviceWorker.register('static/sw.min.js');
	return swRegistration;
}

const main = async () => {
	check();
	const swRegistration = await registerServiceWorker();
}

main();