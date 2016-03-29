l = 7
h = 6
pl = 4


def mkBoard():
    board = [[0 for x in range(h)] for x in range(l)]
        return board

	def copyBoard(board, flip = False):
	    b = [[0 for x in range(h)] for x in range(l)]
	        for y in range(h):
		        for x in range(l):
			            if not flip:
				                    b[x][y] = board[x][y]
						                elif board[x][y] == 1:
								                b[x][y] = 2
										            elif board[x][y] == 2:
											                    b[x][y] = 1
													                else:
															                b[x][y] = 0
																	                
																			    return b


																			    def printBoard(board, pretty = True, switch=False):
																			        for y in range(h):
																				        for x in range(l):
																					            s = board[x][y]
																						                if pretty:
																								                if s == 0:
																										                    s = "."
																												                    elif (s == 1 and switch is False) or (s == 2 and switch is True):
																														                        s = "X"
																																	                elif (s == 2 and switch is False) or (s == 1 and switch is True):
																																			                    s = "O"
																																					                    else:
																																							                        s = "?"
																																										                
																																												            print(s, end="")
																																													            print("")

																																														    def boardToTuple(board):

																																														        def inti(i):
																																															        i0 = board[0][i] % 4
																																																        i1 = (board[1][i] % 4) << 2
																																																	        i2 = (board[2][i] % 4) << 4
																																																		        i3 = (board[3][i] % 4) << 6
																																																			        i4 = (board[4][i] % 4) << 8
																																																				        i5 = (board[5][i] % 4) << 10
																																																					        i6 = (board[6][i] % 4) << 12
																																																						        i7 = (board[0][i+1] % 4) << 14
																																																							        i8 = (board[1][i+1] % 4) << 16
																																																								        i9 = (board[2][i+1] % 4) << 18
																																																									        i10 = (board[3][i+1] % 4) << 20
																																																										        i11 = (board[4][i+1] % 4) << 22
																																																											        i12 = (board[5][i+1] % 4) << 24
																																																												        i13 = (board[6][i+1] % 4) << 26

																																																													        int1 = i0 + i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + \
																																																														        i10 + i11 + i12 + i13
																																																															        return int1

																																																																    return (inti(0), inti(2), inti(4))

																																																																    def tupleToBoard(tuple_):

																																																																        board = [[0 for x in range(h)] for x in range(l)]

																																																																	    def toBoard(board, i, t):
																																																																	            board[0][i] = (t % 4)
																																																																		            board[1][i] = (t >> 2) % 4
																																																																			            board[2][i] = (t >> 4) % 4
																																																																				            board[3][i] = (t >> 6) % 4
																																																																					            board[4][i] = (t >> 8) % 4
																																																																						            board[5][i] = (t >> 10) % 4
																																																																							            board[6][i] = (t >> 12) % 4
																																																																								            board[0][i+1] = (t >> 14) % 4
																																																																									            board[1][i+1] = (t >> 16) % 4
																																																																										            board[2][i+1] = (t >> 18) % 4
																																																																											            board[3][i+1] = (t >> 20) % 4
																																																																												            board[4][i+1] = (t >> 22) % 4
																																																																													            board[5][i+1] = (t >> 24) % 4
																																																																														            board[6][i+1] = (t >> 26) % 4

																																																																															        toBoard(board, 0, tuple_[0])
																																																																																    toBoard(board, 2, tuple_[1])
																																																																																        toBoard(board, 4, tuple_[2])
																																																																																	    return board

																																																																																	    def isFull(board):
																																																																																	        for x in range(pl): #todo change
																																																																																		        if board[x][0] == 0:
																																																																																			            return False
																																																																																				        return True

																																																																																					def isWinner(board, i):
																																																																																					    for y in range(h):
																																																																																					            for x in range(l-3):
																																																																																						                if board[x][y] == i and board[x+1][y] == i and board[x+2][y] == i and board[x+3][y] == i :
																																																																																								                return True

																																																																																										    for y in range(h-3):
																																																																																										            for x in range(l):
																																																																																											                if board[x][y] == i and board[x][y+1] == i and board[x][y+2] == i and board[x][y+3] == i :
																																																																																													                return True

																																																																																															    for y in range(h-3):
																																																																																															            for x in range(l-3):
																																																																																																                if board[x][y] == i and board[x+1][y+1] == i and board[x+2][y+2] == i and board[x+3][y+3] == i :
																																																																																																		                return True

																																																																																																				    for y in range(h-3):
																																																																																																				            for x in range(l-3):
																																																																																																					                x2 = x+3
																																																																																																							            if board[x2][y] == i and board[x2-1][y+1] == i and board[x2-2][y+2] == i and board[x2-3][y+3] == i :
																																																																																																								                    return True

																																																																																																										        return False

																																																																																																											def getWinner(board):
																																																																																																											    if isWinner(board, 1):
																																																																																																											            #if isWinner(board, 2):
																																																																																																												             #   raise "error"
																																																																																																													             return 1

																																																																																																														         if isWinner(board, 2):
																																																																																																															         return 2

																																																																																																																     return 0

																																																																																																																     def appendToBoard(board, x_pos, value):
																																																																																																																         if value != 1 and value !=2:
																																																																																																																	         raise Exception("error incorrect value to append")

																																																																																																																		     i = h-1
																																																																																																																		         ok = False
																																																																																																																			     
																																																																																																																			         while i>=0:
																																																																																																																				         if board[x_pos][i] == 0:
																																																																																																																					             board[x_pos][i] = value
																																																																																																																						                 ok = True
																																																																																																																								             break
																																																																																																																									             i -= 1

																																																																																																																										         if not ok:
																																																																																																																											         raise Exception("error no place on board")

																																																																																																																												     
																																																																																																																												         

																																																																																																																													 board = mkBoard()
																																																																																																																													 t = boardToTuple(board)

																																																																																																																													 state0 = board


																																																																																																																													 memoize_dict = {}

																																																																																																																													 total = 0
																																																																																																																													 totalInd = 0


																																																																																																																													 def compute(board):

																																																																																																																													     global total
																																																																																																																													         global totalInd
																																																																																																																														     global memoize_dict
																																																																																																																														         
																																																																																																																															     total+=1
																																																																																																																															         if total %100000 == 0:
																																																																																																																																         print("total = " + str(total))
																																																																																																																																	         
																																																																																																																																		     #print("===")
																																																																																																																																		         #print(state[0])
																																																																																																																																			     #printBoard(board)

																																																																																																																																			         compressedState = boardToTuple(board)
																																																																																																																																				     if compressedState in memoize_dict:
																																																																																																																																				             return memoize_dict[compressedState]

																																																																																																																																					         totalInd += 1
																																																																																																																																						     if totalInd %100000 == 0:
																																																																																																																																						             print("individual total = " + str(totalInd))
																																																																																																																																							         
																																																																																																																																								     if isWinner(board, 1):
																																																																																																																																								             memoize_dict[compressedState] = (True, [])
																																																																																																																																									             return (True, [])
																																																																																																																																										         
																																																																																																																																											     if isWinner(board, 2):
																																																																																																																																											             memoize_dict[compressedState] = (False, [])
																																																																																																																																												             return (False, [])

																																																																																																																																													         if isFull(board):
																																																																																																																																														         memoize_dict[compressedState] = (None, [])
																																																																																																																																															         return (None, [])

																																																																																																																																																     ll = []
																																																																																																																																																         
																																																																																																																																																	     for x in range(pl): #todo restore l 
																																																																																																																																																	             if board[x][0] == 0:
																																																																																																																																																		                 board2 = copyBoard(board, flip=True)
																																																																																																																																																				             appendToBoard(board2, x, 2)
																																																																																																																																																					                 (res, stateList) = compute(board2)
																																																																																																																																																							             if res is False:
																																																																																																																																																								                     stateList2 = stateList.copy()
																																																																																																																																																										                     stateList2.append(compressedState)
																																																																																																																																																												                     memoize_dict[compressedState] = (True, stateList2)
																																																																																																																																																														                     return (True, stateList2)
																																																																																																																																																																                 ll.append((res, stateList))

																																																																																																																																																																		     for (opp_res, stateList) in ll:
																																																																																																																																																																		             if opp_res == None:
																																																																																																																																																																			                 stateList2 = stateList.copy()
																																																																																																																																																																					             stateList2.append(compressedState)
																																																																																																																																																																						                 memoize_dict[compressedState] = (None, stateList2)
																																																																																																																																																																								             return (None, stateList2)

																																																																																																																																																																									         stateList2 = ll[0][1].copy()
																																																																																																																																																																										     stateList2.append(compressedState)
																																																																																																																																																																										         memoize_dict[compressedState] = (False, stateList2)
																																																																																																																																																																											     return (False,  stateList2)

																																																																																																																																																																											     a = compute(state0)

																																																																																																																																																																											     def debugStateList(res):
																																																																																																																																																																											         stateList = res[1]
																																																																																																																																																																												     it = 0
																																																																																																																																																																												         switch = True
																																																																																																																																																																													     for i in reversed(stateList):
																																																																																																																																																																													             print(it)
																																																																																																																																																																														             it +=1
																																																																																																																																																																															             printBoard(tupleToBoard(i[1]), switch=switch)
																																																																																																																																																																																             switch = not switch
																																																																																																																																																																																	             print("")

																																																																																																																																																																																		     for key, value in memoize_dict.items():
																																																																																																																																																																																		         print(key[0])
																																																																																																																																																																																			     printBoard(tupleToBoard(key[1]))
																																																																																																																																																																																			         print(value)
																																																																																																																																																																																				     print("_______________")
																																																																																																																																																																																				         break

																																																																																																																																																																																					 debugStateList(a)


