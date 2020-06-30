document.addEventListener("DOMContentLoaded", function () {
	$(".website-body").css("display", "none");
	$(".footer-section").css("display", "none");
	$(".website-body").fadeIn(750);
	$(".footer-section").fadeIn(750);

	$(".header-section a.nav-link").click(function (event) {
		event.preventDefault();
		linkLocation = this.href;
		$(".footer-section").fadeOut(750);
		$(".website-body").fadeOut(750, redirectPage);
	});

	$(".slide").click(function (event) {
		event.preventDefault();
		linkLocation = this.href;
		$(".footer-section").fadeOut(750);
		$(".website-body").fadeOut(750, redirectPage);
	});

	$(".slide-scrolling").click(function (event) {
		event.preventDefault();
		linkLocation = this.href;

		$('html, body').animate({ scrollTop: 0 }, 1000);
		setTimeout(function () {
			$(".footer-section").fadeOut(750);
			$(".website-body").fadeOut(750, redirectPage);
		}, 1000);
	});

	$(".footer-section a.nav-link").click(function (event) {
		event.preventDefault();
		linkLocation = this.href;

		$('html, body').animate({ scrollTop: 0 }, 1000);
		setTimeout(function () {
			$(".footer-section").fadeOut(750);
			$(".website-body").fadeOut(750, redirectPage);
		}, 1000);
	});

	function redirectPage() {
		window.location = linkLocation;
	}

	$("#callback-form").fancybox();

	$('.actual_news-carousel').slick({
		dots: false,
		arrows: true,
		infinite: true,
		slidesToShow: 3,
		slidesToScroll: 1
	});

	$('.about-us__feedback-carousel').slick({
		dots: false,
		arrows: true,
		infinite: true,
		slidesToShow: 3,
		slidesToScroll: 1
	});

	$('.category-info__main-photo-carousel').slick({
		arrows: false,
		fade: true,
		slidesToShow: 1,
		slidesToScroll: 1,
		asNavFor: '.category-info__photo-preview-carousel'
	});
	
	$('.category-info__photo-preview-carousel').slick({
		dots: false,
		arrows: true,
		infinite: true,
		slidesToShow: 4,
		slidesToScroll: 1,
		focusOnSelect: true,
		asNavFor: '.category-info__main-photo-carousel'
	});

	$(".newsfeed__display--list").click(function () {
		if ($(".newsfeed__display--tile").hasClass("active")) {

			$(".newsfeed__display--tile").prop("disabled", true);
			$(".newsfeed--tile").css('opacity', '0');

			setTimeout(function () {
				$(".newsfeed--tile").addClass('hide');
				$(".newsfeed--list").removeClass('hide');
			}, 750);
			setTimeout(function () {
				$(".newsfeed--list").css('opacity', '1');
			}, 1000);


			$(".newsfeed__display--list").addClass("active");
			$(".newsfeed__display--tile").removeClass("active");

			setTimeout(function () {
				$(".newsfeed__display--tile").prop("disabled", false);
			}, 1500);
		}
	});

	$(".newsfeed__display--tile").click(function () {
		if ($(".newsfeed__display--list").hasClass("active")) {

			$(".newsfeed__display--list").prop("disabled", true);
			$(".newsfeed--list").css('opacity', '0');

			setTimeout(function () {
				$(".newsfeed--list").addClass('hide');
				$(".newsfeed--tile").removeClass('hide');
			}, 750);
			setTimeout(function () {
				$(".newsfeed--tile").css('opacity', '1');
			}, 1000);

			$(".newsfeed__display--tile").addClass("active");
			$(".newsfeed__display--list").removeClass("active");

			setTimeout(function () {
				$(".newsfeed__display--list").prop("disabled", false);
			}, 1500);
		}
	});

	$(".eventsfeed__display--list").click(function () {
		if ($(".eventsfeed__display--tile").hasClass("active")) {

			$(".eventsfeed__display--tile").prop("disabled", true);
			$(".eventsfeed--tile").css('opacity', '0');

			setTimeout(function () {
				$(".eventsfeed--tile").addClass('hide');
				$(".eventsfeed--list").removeClass('hide');
			}, 750);
			setTimeout(function () {
				$(".eventsfeed--list").css('opacity', '1');
			}, 1000);


			$(".eventsfeed__display--list").addClass("active");
			$(".eventsfeed__display--tile").removeClass("active");

			setTimeout(function () {
				$(".eventsfeed__display--tile").prop("disabled", false);
			}, 1500);
		}
	});

	$(".eventsfeed__display--tile").click(function () {
		if ($(".eventsfeed__display--list").hasClass("active")) {

			$(".eventsfeed__display--list").prop("disabled", true);
			$(".eventsfeed--list").css('opacity', '0');

			setTimeout(function () {
				$(".eventsfeed--list").addClass('hide');
				$(".eventsfeed--tile").removeClass('hide');
			}, 750);
			setTimeout(function () {
				$(".eventsfeed--tile").css('opacity', '1');
			}, 1000);

			$(".eventsfeed__display--tile").addClass("active");
			$(".eventsfeed__display--list").removeClass("active");

			setTimeout(function () {
				$(".eventsfeed__display--list").prop("disabled", false);
			}, 1500);
		}
	});

});
