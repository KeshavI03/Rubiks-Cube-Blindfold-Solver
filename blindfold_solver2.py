# Example Scramble: D2 U F' B D R' U R' U2 B' R' L F U R D2 F' L U' B L B D2 R2 B'   (green face towards white top dont forget to reorient after)

def get_corners(b_face, r_face, y_face, o_face, w_face, g_face):

	cr = []
	cr.append(''.join([b_face[0][0] ,w_face[0][0] ,o_face[0][2] ]))
	cr.append(''.join([b_face[0][2] ,o_face[0][0] ,y_face[0][2] ]))
	cr.append(''.join([b_face[2][2] ,y_face[0][0] ,r_face[0][2] ]))
	cr.append(''.join([b_face[2][0] ,r_face[0][0] ,w_face[0][2] ]))

	cr.append(''.join([g_face[0][0] ,w_face[2][2] ,r_face[2][0] ]))
	cr.append(''.join([g_face[0][2] ,r_face[2][2] ,y_face[2][0] ]))
	cr.append(''.join([g_face[2][2] ,y_face[2][2] ,o_face[2][0] ]))
	cr.append(''.join([g_face[2][0] ,o_face[2][2] ,w_face[2][0] ]))

	return cr	



def get_edges(b_face, r_face, y_face, o_face, w_face, g_face):

	ed = []
	ed.append(''.join([b_face[0][1] , o_face[0][1] ]))
	ed.append(''.join([b_face[1][2] , y_face[0][1] ]))
	ed.append(''.join([b_face[2][1] , r_face[0][1] ]))
	ed.append(''.join([b_face[1][0] , w_face[0][1] ]))

	ed.append(''.join([w_face[1][0] , o_face[1][2] ]))
	ed.append(''.join([o_face[1][0] , y_face[1][2] ]))
	ed.append(''.join([y_face[1][0] , r_face[1][2] ]))
	ed.append(''.join([r_face[1][0] , w_face[1][2] ]))

	ed.append(''.join([g_face[0][1] , r_face[2][1] ]))
	ed.append(''.join([g_face[1][2] , y_face[2][1] ]))
	ed.append(''.join([g_face[2][1] , o_face[2][1] ]))
	ed.append(''.join([g_face[1][0] , w_face[2][1] ]))

	return ed




c_default =['bwo','boy','byr','brw','gwr','gry','gyo','gow']

l_ar = 'aqnbmjcifderushvglwkpxot'

e_default =['rw','br','ob','oy','yr','gw','gr','by','ow','og','bw','yg']

e_ar = 'ambicedqtnpjlfhrugvkwoxs'



# Function generates letter (a-x) from the three colors of a given corner
# First letter determines which side of the corner we are talking about:
# (['b', 'w', 'o']) will return 'a' and so will (['b', 'o', 'w']), but (['o', 'b', 'w']) returns 'n'

# Get the neccessary letter position for any corner given its three colors (first color will be the one you are looking at)
def c_to_l(letters):

	face_combos =  ['woyr', 'wbyg', 'rbog', 'ybwg', 'obrg', 'wryo']
	faces = 'bryowg'
	pos = faces.index(letters[0])

	for i in range(0,4):
		if face_combos[pos][i%4] in letters and face_combos[pos][(i+1)%4] in letters:
			return chr(97+pos*4+i)

	return 0


def e_to_l(letters):

	face_combos =  ['oyrw', 'bygw', 'bogr', 'bwgy', 'brgo', 'ryow']
	faces = 'bryowg'

	pos = faces.index(letters[0])
	pos_color = face_combos[pos].index(letters[1])

	return chr(97+pos*4+pos_color)


def l_to_c(l, arr):
	pos = l_ar.index(l)

	num = int(pos/3)
	num_l = pos%3

	# print
	return ''.join([arr[num][num_l%3], arr[num][(num_l+1) %3], arr[num][(num_l+2) %3]])


def l_to_e(l, arr):

	pos = e_ar.index(l)

	num = int(pos/2)
	num_l = pos%2

	return ''.join([arr[num][num_l%2] , arr[num][(num_l+1)%2]])


def solve_corners(c):
	code_word = ''

	tests = 'ajcrulpt'
	solved = [1, 0, 0, 0, 0, 0, 0, 0]

	for i in range(0,8):
		if c_to_l(l_to_c(tests[i], c)) == tests[i]: solved[i] = 1

	let = 'a'
	while 0 in solved:
	# for l in range(0, 20):
		let = c_to_l(l_to_c(let, c))
		c_num = int(l_ar.index(let)/3)
		if c_num != 0: code_word += let


		if solved[c_num] == 1:
			c_num = solved.index(0)
			let = tests[c_num]
			solved[c_num] = 1
			code_word += let

		solved[c_num] = 1

	let = c_to_l(l_to_c(let, c))
	c_num = int(l_ar.index(let)/3)
	if c_num != 0: code_word += let

	return code_word


def solve_edge(e):
	code_word = ''

	tests = 'abcdnjlhuvwx'
	solved = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	for i in range(0, 12):
		if e_to_l(l_to_e(tests[i], e)) == tests[i]: solved[i] = 1

	let = 'b'
	while 0 in solved:

		let = e_to_l(l_to_e(let, e))
		e_num = int(e_ar.index(let)/2)

		if e_num != 1: code_word += let


		if solved[e_num] == 1:
			e_num = solved.index(0)
			let = tests[e_num]
			solved[e_num] = 1
			code_word += let

		solved[e_num] = 1

	let = e_to_l(l_to_e(let, e))
	e_num = int(e_ar.index(let)/2)

	if e_num != 1: code_word += let

	return code_word


def solve(b, r, y, o, w, g):

	print(solve_corners(get_corners(b, r, y, o, w, g)))
	print('----')
	print(solve_edge(get_edges(b, r, y, o, w, g)))

# print(get_corners())

# print(get_edges())

# b = ['brg',
# 	 'wbb',
# 	 'bry']

# r = ['rgg',
# 	 'orr',
# 	 'bbr']

# y = ['oyr',
# 	 'byr',
# 	 'yyo']

# o = ['wyy',
# 	 'wog',
# 	 'byo']

# w = ['oow',
# 	 'wwg',
# 	 'wor']

# g = ['ywg',
# 	 'bgg',
# 	 'gow']

# solve(b, r, y, o, w, g)