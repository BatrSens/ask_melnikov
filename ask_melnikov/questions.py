def answs(qq):
    answers = []
    for j in xrange(0, qq):
        answers.append({
            'text': "JUST DO IT!!!",
            'id': j,
            'nickname': "S.LaBeouf",
            'likes': 4,
            'avatar': "/img/avatar2.jpg",
            'rating': 7,
        })
    return answers

questions = []
for i in xrange (0, 43):
    ans = i % 8
    questions.append({
        'title': "How to build a house?",
        'id': i,
        'text': "I'm sick of living in a box. How to build a house? Well, where do I start?",
        'rating': 8,
        'answers_count': ans,
        'tags': ["house", "livingroom"],
        'nickname': "R.Darbyshire",
        'likes': 5,
        'avatar': "/img/avatar1.png",
        'answers': answs(ans)
    })