document.addEventListener("DOMContentLoaded", function () {

	$('.actual_news-carousel').slick({
		dots: false,
		arrows: true,
		
		// prevArrow: '<button type="button" class="slick-prev"></button>',
		// nextArrow: '<button type="button" class="slick-next"></button>',

        infinite: true,
		slidesToShow: 3,
		slidesToScroll: 1
	});

});
