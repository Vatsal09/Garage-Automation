var path = 'http://www.lucashanyok.com/images_1/',
    imgs = ['carrot.gif','neil_1.jpg','steak.jpg'],
    i = Math.floor(Math.random()*imgs.length);
$('.el').append("<img src='"+path+imgs[i]+"'>");

var AlbumsListPage = {
	init: function() {
		this.$container = $('.albums-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

	bindEvents: function() {
		$('.btn-favorite', this.$container).on('click', function(e) {
			e.preventDefault();

			var self = $(this);
			var url = $(this).attr('href');
			$.getJSON(url, function(result) {
				if (result.success) {
					$('.glyphicon-star', self).toggleClass('active');
				}
			});

			return false;
		});
	}
};

var SongsListPage = {
	init: function() {
		this.$container = $('.songs-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

	bindEvents: function() {
		$('.btn-favorite', this.$container).on('click', function(e) {
			e.preventDefault();

			var self = $(this);
			var url = $(this).attr('href');
			$.getJSON(url, function(result) {
				if (result.success) {
					$('.glyphicon-star', self).toggleClass('active');
				}
			});

			return false;
		});
	}
};

$(document).ready(function() {
	AlbumsListPage.init();
	SongsListPage.init();
});

// var data = "{{data_set|safe}}";
// var level = "{{level|safe}}"
// var companies = '{{ spots1|escapejs }}';
