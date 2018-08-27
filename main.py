####### Python 3.6
####### author: Rafael Calixto
####### created at: 08/24/2018
####### description: This is the main file of the project Python
####### Challenge WiseTrust.

from bottle import route, run, get, post, request

from scraper import Scraper
from text_minning import Minner, Word_count, Word_classifier
from show_analyses import Table, Chart

### The bottle library is user here to create a graphic interface to the project
class GUI():
    # At http://localhost:8080 you can access the intro page of the project
    @route('/')
    def index():
        return 'Python Challenge WiseTrust'

    # The search tool is located at http://localhost:8080/search
    @get('/search')
    def search():
        return open('gui_template.html').read()

    @post('/search')
    def get_url():
        url = request.forms.get('URL')
        data, err = Scraper().get_it(url)
        if err is not None:
            return err
        text =  Minner.dig(data)
        word_count = Word_count.count(text)
        class_words = Word_classifier.classify(text)
        table = Table.show(word_count, class_words)
        Chart.show(word_count)

        return table

    run(host='localhost', dpi = 100000, port=8080)

GUI().index()
