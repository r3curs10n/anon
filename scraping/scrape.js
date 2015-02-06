function get_author(answer_box){
	var author_box = answer_box.find('.author_info')
	var author_link = author_box.children().first()
	return author_link.attr('href').substring(1)
}

function get_permalink(answer_box){
	var question_link = answer_box.find('.question_link')
	var author = get_author(answer_box)
	return [question_link.attr('href').substring(1), 'answer', author].join('/')
}

function get_answers(){
	var question_links = $('.UserAnswerProfileFeed').find('.question_link')
	return question_links.parents('.AnswerListItem')
}

function get_answer_permalinks(){
	return get_answers().map(function(){
		return get_permalink($(this))
	})
}

var answers_permalinks = {}

function collect_answer_permalinks(){
	var links = get_answer_permalinks()
	console.log()
	links.each(function(){
		answers_permalinks[this] = true
	})
}

$(document).ready(function(){
	$('body').append("<input id='SendPermalinks' type='button' value='Send' style='position: fixed; top: 100px; left: 0;' />")
	$('body').append("<input id='CollectPermalinks' type='button' value='Collect' style='position: fixed; top: 120px; left: 0;' />")
	
	$('#SendPermalinks').click(function(){
		var permalink_list = []
		for (var key in answers_permalinks) {
			if (answers_permalinks.hasOwnProperty(key)) {
				permalink_list.push(key)
			}
		}
		var data_to_send = permalink_list.join('#')
		console.log(data_to_send)
		$.ajax({
			type: 'POST',
			url: 'http://172.16.27.31:8080/scraper/newlinks',
			data: {links: data_to_send}
		})
	})

	$('#CollectPermalinks').click(function(){
		collect_answer_permalinks()
		var count = 0
		for (var key in answers_permalinks) {
			if (answers_permalinks.hasOwnProperty(key)) {
				count++
			}
		}
		$(this).attr('value', 'Collect (' + count + ')')
	})
})