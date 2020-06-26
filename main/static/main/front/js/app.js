document.addEventListener("DOMContentLoaded", function () {

	$('.actual_news-carousel').slick({
		dots: false,
		arrows: true,
		infinite: true,
		slidesToShow: 3,
		slidesToScroll: 1
	});

	$(".newsfeed__display--list").click(function() {
		if ($(".newsfeed__display--tile").hasClass("active")) {

			$(".newsfeed__display--tile").prop("disabled", true);
			$(".newsfeed--tile").css('opacity', '0');

			setTimeout(function (){
				$(".newsfeed--tile").addClass('hide');
				$(".newsfeed--list").removeClass('hide');
			}, 750);
			setTimeout(function (){
				$(".newsfeed--list").css('opacity', '1');
			}, 1000);
			

			$(".newsfeed__display--list").addClass("active");
			$(".newsfeed__display--tile").removeClass("active");

			setTimeout(function (){
				$(".newsfeed__display--tile").prop("disabled", false);
			}, 1500);
		}
	});

	$(".newsfeed__display--tile").click(function() {
		if ($(".newsfeed__display--list").hasClass("active")) {

			$(".newsfeed__display--list").prop("disabled", true);
			$(".newsfeed--list").css('opacity', '0');

			setTimeout(function (){
				$(".newsfeed--list").addClass('hide');
				$(".newsfeed--tile").removeClass('hide');
			}, 750);
			setTimeout(function (){
				$(".newsfeed--tile").css('opacity', '1');
			}, 1000);

			$(".newsfeed__display--tile").addClass("active");
			$(".newsfeed__display--list").removeClass("active");

			setTimeout(function (){
				$(".newsfeed__display--list").prop("disabled", false);
			}, 1500);
		}
	});

});
