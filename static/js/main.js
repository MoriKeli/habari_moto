document.addEventListener('DOMContentLoaded', () => {
	"use strict";

	// sticky header on scroll
	const selectHeader = document.querySelector('#header');
	if (selectHeader) {
		document.addEventListener('scroll', () => {
			window.scrollY > 100 ? selectHeader.classList.add('sticked') : selectHeader.classList.remove('sticked');
		});
	}

	// mobile nav toggle
	const mobileNavToogleButton = document.querySelector('.mobile-nav-toggle');

	if (mobileNavToogleButton) {
			mobileNavToogleButton.addEventListener('click', function(event) {
			event.preventDefault();
			mobileNavToogle();
		});
	}

	function mobileNavToogle() {
		document.querySelector('body').classList.toggle('mobile-nav-active');
		mobileNavToogleButton.classList.toggle('bi-list');
		mobileNavToogleButton.classList.toggle('bi-x');
	}

	// hide mobile nav on same-page/hash links
	document.querySelectorAll('#navbar a').forEach(navbarlink => {
		if (!navbarlink.hash) return;

		let section = document.querySelector(navbarlink.hash);
		if (!section) return;

		navbarlink.addEventListener('click', () => {
			if (document.querySelector('.mobile-nav-active')) {
				mobileNavToogle();
			}
		});
	});

	// toggle mobile nav dropdowns
	const navDropdowns = document.querySelectorAll('.navbar .dropdown > a');

	navDropdowns.forEach(el => {
		el.addEventListener('click', function(event) {
			if (document.querySelector('.mobile-nav-active')) {
				event.preventDefault();
				this.classList.toggle('active');
				this.nextElementSibling.classList.toggle('dropdown-active');

				let dropDownIndicator = this.querySelector('.dropdown-indicator');
				dropDownIndicator.classList.toggle('bi-chevron-up');
				dropDownIndicator.classList.toggle('bi-chevron-down');
			}
		})
	});
	
	// back to top button
	const scrollTop = document.querySelector('.back-to-top');
	if (scrollTop) {
		const togglescrollTop = function() {
			window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
		}
		window.addEventListener('load', togglescrollTop);
		document.addEventListener('scroll', togglescrollTop);
		scrollTop.addEventListener('click', window.scrollTo({
		top: 0,
		behavior: 'smooth'
		}));
	}

	// open and close search form
	const searchOpen = document.querySelector('.js-search-open');
	const searchClose = document.querySelector('.js-search-close');
	const searchWrap = document.querySelector(".js-search-form-wrap");

	searchOpen.addEventListener("click", (e) => {
		e.preventDefault();
		searchWrap.classList.add("active");
	});

	searchClose.addEventListener("click", (e) => {
		e.preventDefault();
		searchWrap.classList.remove("active");
	});

	// initiate Glightbox
	const glightbox = GLightbox({
		selector: '.glightbox'
	});

	// animation on scroll (aos)
	function aos_init() {
		AOS.init({
			duration: 1000,
			easing: 'ease-in-out',
			once: true,
			mirror: false
		});
	}
	window.addEventListener('load', () => {
		aos_init();
	});

});