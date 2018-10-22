from die import Die
import pygal

def once_result(dielist=[]):
	result = 0
	for die in dielist:
		result = result+die.roll()
	return result

def get_results(dielist=[], nums=100):
	results = [ once_result(dielist) for num in range(nums)]
	return results

def get_maxside(dielist=[]):
	_max = 0
	for die in dielist:
		_max = _max + die.num_side
	return _max+1

def get_analys(dielist=[], results=[]):
	freqs = [results.count(value) for value in range(len(dielist), get_maxside(dielist))]
	return freqs

'''
dielists = [Die(8),Die(8),Die(8)]
results = get_results(dielist=dielists, nums=1000000)
freqs = get_analys(dielist=dielists, results=results)


hist = pygal.Bar()
hist._title = "Results of rolling D10 D6 1000 times"
hist.x_labels = list(range(len(dielists),get_maxside(dielists)))
hist._x_title = 'Result'
hist._y_title = 'Frequency of result'

hist.add('D6+D10', freqs)
hist.render_to_file('die_visual.svg')

print(sum(freqs))
print(freqs)
'''