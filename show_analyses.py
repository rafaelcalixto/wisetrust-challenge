####### Python 3.6
####### author: Rafael Calixto
####### created at: 08/24/2018
####### description: This library contains objects to build the graphic answers
####### to the challenge.

from matplotlib import pyplot

class Table:
    '''The Table object provide an string with an html table listing all words
       found in the page, his frequency and his gramatical type'''
    def show(dict_fq, list_type):
        ### input: dict, lit
        ### output: str {html code}
        template = open('table_template.html').read()
        tags = '<tr><td>{x}</td><td>{y}</td><td>{z}</td></tr>'
        rows = []
        words_fw = tuple(dict_fq.keys())
        for word, wtype in list_type:
            if word.isalpha():
                freq = str(dict_fq[word]) if word in words_fw else ''
                new_line = tags.format_map({'x':word, 'y':wtype, 'z':freq})
                if new_line not in tuple(rows):
                    rows.append(new_line)
        return template.format_map({'x' : ''.join(rows)})

class Chart:
    '''The Chart object plot a histogram with the first 100 most common words
       in the text of the web page crawled'''
    def show(dict_fq):
        ### input: dict
        ### output: None
        word = []
        freq = []
        limit = len(dict_fq) if len(dict_fq) < 100 else 100
        data = list(
                    reversed(
                            sorted(dict_fq.items(), key = lambda w: w[1])
                            )
                    )[:limit]
        for x, y in data:
            word.append(x)
            freq.append(y)

        pyplot.rcdefaults()
        fig, ax = pyplot.subplots()
        ax.barh(range(0,len(word)), freq)
        ax.set_yticks(range(0,len(word)))
        ax.set_yticklabels(word)
        ax.invert_yaxis()
        ax.set_xlabel('Frequency')
        ax.set_title('Most Frequency Words')
        pyplot.show()
