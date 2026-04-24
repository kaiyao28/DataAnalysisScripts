import numpy as np

# ── CREATE ARRAYS ──────────────────────────────────────────────────────────────
np.array([1, 2, 3])
np.zeros((3, 4))
np.ones((3, 4))
np.full((3, 4), 7)
np.eye(3)                                  # identity matrix
np.arange(0, 10, 2)                        # [0, 2, 4, 6, 8]
np.linspace(0, 1, 50)                      # 50 evenly spaced between 0 and 1

np.random.seed(42)
np.random.rand(3, 4)                       # uniform [0, 1)
np.random.randn(3, 4)                      # standard normal
np.random.randint(0, 10, size=(3, 4))
np.random.choice([1, 2, 3], size=10, replace=True)

# ── SHAPE & RESHAPE ────────────────────────────────────────────────────────────
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape                                    # (2, 3)
a.ndim                                     # 2
a.size                                     # 6
a.dtype

a.reshape(3, 2)
a.flatten()                                # always returns copy
a.ravel()                                  # returns view when possible
a.T                                        # transpose

np.expand_dims(a, axis=0)                  # (1, 2, 3)
a[np.newaxis, :]                           # same as above
a.squeeze()                                # remove dimensions of size 1

# ── INDEXING & SLICING ─────────────────────────────────────────────────────────
a[0]                                       # first row
a[:, 1]                                    # second column
a[0, 2]                                    # element at row 0, col 2
a[1:, :2]                                  # slicing

# boolean indexing
a[a > 3]
a[(a > 1) & (a < 5)]

# fancy indexing
a[[0, 1], [2, 0]]                          # elements (0,2) and (1,0)
np.where(a > 3, a, 0)                      # conditional: keep if > 3, else 0

# ── MATH ───────────────────────────────────────────────────────────────────────
np.add(a, b)          # or a + b
np.subtract(a, b)     # or a - b
np.multiply(a, b)     # or a * b  (element-wise)
np.dot(a, b)          # matrix multiplication
a @ b                 # same as dot for 2D
np.matmul(a, b)

np.sqrt(a)
np.exp(a)
np.log(a)
np.log2(a)
np.log10(a)
np.abs(a)
np.power(a, 2)
np.clip(a, 0, 5)                           # clamp values

# ── STATISTICS ─────────────────────────────────────────────────────────────────
a = np.array([[1, 2, 3], [4, 5, 6]])

np.sum(a)                                  # all elements
np.sum(a, axis=0)                          # column sums
np.sum(a, axis=1)                          # row sums

np.mean(a)
np.mean(a, axis=0)
np.median(a)
np.std(a)
np.var(a)
np.min(a)
np.max(a)
np.argmin(a)                               # index of min
np.argmax(a)                               # index of max

np.percentile(a, 25)
np.percentile(a, [25, 50, 75])
np.corrcoef(a[0], a[1])                    # correlation matrix
np.cov(a[0], a[1])                         # covariance matrix
np.unique(a)
np.unique(a, return_counts=True)

# ── COMBINE / STACK ────────────────────────────────────────────────────────────
np.concatenate([a, b], axis=0)             # stack rows
np.concatenate([a, b], axis=1)             # stack cols
np.vstack([a, b])                          # vertical stack (rows)
np.hstack([a, b])                          # horizontal stack (cols)
np.stack([a, b], axis=0)                   # new axis

# ── SORTING ────────────────────────────────────────────────────────────────────
np.sort(a)                                 # sort each row
np.sort(a, axis=0)                         # sort each column
np.argsort(a)                              # indices that would sort array

# ── LINEAR ALGEBRA ─────────────────────────────────────────────────────────────
np.linalg.inv(a)                           # matrix inverse
np.linalg.det(a)                           # determinant
np.linalg.norm(a)                          # Frobenius norm
np.linalg.norm(a, axis=1)                  # row-wise L2 norm
eigenvalues, eigenvectors = np.linalg.eig(a)
U, S, Vt = np.linalg.svd(a)               # SVD

# ── TYPE CONVERSION ────────────────────────────────────────────────────────────
a.astype(np.float32)
a.astype(np.int64)
np.nan_to_num(a)                           # replace NaN/inf with 0
np.isnan(a)
np.isinf(a)
np.isfinite(a)
