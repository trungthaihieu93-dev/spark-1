import parallel_compressed
from dumb25519 import random_point, random_scalar, PointVector
from random import randrange
import unittest

class TestParallelCompressed(unittest.TestCase):
	def test_complete(self):
		params = parallel_compressed.ParallelCompressedParameters(random_point(),2,4)
		N = params.n**params.m

		l = randrange(0,N)
		s = random_scalar()
		v = random_scalar()
		witness = parallel_compressed.ParallelCompressedWitness(l,s,v)
		
		S = PointVector([random_point() for _ in range(N)])
		V = PointVector([random_point() for _ in range(N)])
		S[l] = s*params.F
		V[l] = v*params.F
		statement = parallel_compressed.ParallelCompressedStatement(params,S,V)

		proof = parallel_compressed.prove(statement,witness)
		parallel_compressed.verify(statement,proof)

if __name__ == '__main__':
	unittest.main()