from markerMap import MarkerMap

# ----------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------- Class Init_trajet_boat ------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------


class Init_trajet_boat(object):

	# contructeur
	# vide

	def __init__(self):
		object.__init__(self)


# ----------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------- Init des 12 trajets ---------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------

# possibilite de rajouter d'autre trajet
# il faudra juste les rajouter au dans la "list_trajets " de la classe "Simulation_bateau"

	def init_trajet_1(self):

		list_t = []
		list_t.append(MarkerMap(630, 583,None))
		list_t.append(MarkerMap(736, 544,None))
		list_t.append(MarkerMap(676, 526,None))
		list_t.append(MarkerMap(727, 310,None))
		list_t.append(MarkerMap(595, 208,None))
		list_t.append(MarkerMap(533, 219,None))
		list_t.append(MarkerMap(433, 2,None))
		list_t.append(MarkerMap(-7, 61,None))
		return list_t

	def init_trajet_2(self):
		list_t = []
		list_t.append(MarkerMap(788, 477,None))
		list_t.append(MarkerMap(690, 454,None))
		list_t.append(MarkerMap(727, 310,None))
		list_t.append(MarkerMap(599, 206,None))
		list_t.append(MarkerMap(882, 135,None))
		list_t.append(MarkerMap(836, 10,None))
		return list_t

	def init_trajet_3(self):
		list_t = []
		list_t.append(MarkerMap(835, 328,None))
		list_t.append(MarkerMap(713, 303,None))
		list_t.append(MarkerMap(595, 204,None))
		list_t.append(MarkerMap(529, 209,None))
		list_t.append(MarkerMap(484, 96,None))
		list_t.append(MarkerMap(411, 128,None))
		list_t.append(MarkerMap(204, 185,None))
		return list_t

	def init_trajet_4(self):
		list_t = []
		list_t.append(MarkerMap(852, 275,None))
		list_t.append(MarkerMap(552, 208,None))
		list_t.append(MarkerMap(731, 169,None))
		list_t.append(MarkerMap(686, 49,None))
		return list_t

	def init_trajet_5(self):
		list_t = []
		list_t.append(MarkerMap(608, 75,None))
		list_t.append(MarkerMap(648, 180,None))
		list_t.append(MarkerMap(542, 204,None))
		list_t.append(MarkerMap(490, 33,None))
		list_t.append(MarkerMap(538, -44,None))
		return list_t

	def init_trajet_6(self):
		list_t = []
		list_t.append(MarkerMap(478, 237,None))
		list_t.append(MarkerMap(451, 241,None))
		list_t.append(MarkerMap(423, 134,None))
		list_t.append(MarkerMap(482, 115,None))
		list_t.append(MarkerMap(509, 189,None))
		list_t.append(MarkerMap(492, 212,None))
		return list_t

	def init_trajet_7(self):
		list_t = []
		list_t.append(MarkerMap(458, 483,None))
		list_t.append(MarkerMap(424, 389,None))
		list_t.append(MarkerMap(452, 380,None))
		list_t.append(MarkerMap(388, 111,None))
		list_t.append(MarkerMap(448, 96,None))
		list_t.append(MarkerMap(419, -45,None))
		return list_t

	def init_trajet_8(self):
		list_t = []
		list_t.append(MarkerMap(-11, -48,None))
		list_t.append(MarkerMap(408, -35,None))
		list_t.append(MarkerMap(490, 61,None))
		list_t.append(MarkerMap(533, 226,None))
		list_t.append(MarkerMap(604, 212,None))
		list_t.append(MarkerMap(725, 321,None))
		list_t.append(MarkerMap(704, 392,None))
		list_t.append(MarkerMap(802, 414,None))
		return list_t

	def init_trajet_9(self):
		list_t = []
		list_t.append(MarkerMap(753, -43,None))
		list_t.append(MarkerMap(449, 31,None))
		list_t.append(MarkerMap(454, 108,None))
		list_t.append(MarkerMap(408, 125,None))
		list_t.append(MarkerMap(439, 260,None))
		list_t.append(MarkerMap(245, 310,None))
		return list_t

	def init_trajet_10(self):
		list_t = []
		list_t.append(MarkerMap(78, 625,None))
		list_t.append(MarkerMap(39, 182,None))
		list_t.append(MarkerMap(119, 118,None))
		list_t.append(MarkerMap(306, 59,None))
		list_t.append(MarkerMap(425, 37,None))
		list_t.append(MarkerMap(495, 112,None))
		list_t.append(MarkerMap(533, 213,None))
		list_t.append(MarkerMap(579, 190,None))
		list_t.append(MarkerMap(553, 100,None))
		return list_t

	def init_trajet_11(self):
		list_t = []
		list_t.append(MarkerMap(-12, 174,None))
		list_t.append(MarkerMap(132, 75,None))
		list_t.append(MarkerMap(295, 40,None))
		list_t.append(MarkerMap(794, -47,None))
		return list_t

	def init_trajet_12(self):

		list_t = []
		list_t.append(MarkerMap(205, 218,None))
		list_t.append(MarkerMap(410, 158,None))
		list_t.append(MarkerMap(418, 84,None))
		list_t.append(MarkerMap(483, 108,None))
		list_t.append(MarkerMap(524, 226,None))
		list_t.append(MarkerMap(651, 205,None))
		list_t.append(MarkerMap(852, 245,None))
		return list_t
