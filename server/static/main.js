$(function () {
	var reviews = $('#reviews');

	reviews.html('Loading Reviews...');

	$.ajax({
		url: '/api/getreviews',
		dataType: 'json',
		success: function (response) {
			reviews.empty(); 
			for(var i = 0; i < response.length; i++) {
				reviews.append(makeReview(response[i]));
			}
		}
	});
});

function makeReview(review) {
	var star = $('<img>').attr('src', 'http://www.kailashhimalaya.com/images/star_icon.png').prop('outerHTML');
	var stars = '';
	for (var i = 0; i < review.stars; i++) {
		stars += star;
	}

	var div = $('<div>').addClass('review');
	div.append($('<div>').addClass('title').html(review.media[0].toUpperCase() + review.media.slice(1) + ' - ' + review.title + ' (' + stars + ')'));
	div.append($('<div>').addClass('content').html(review.review + ' -- <b>' + review.name + '</b>'))
	return div;
}
