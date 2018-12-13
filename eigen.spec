#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : eigen
Version  : 3.3.7
Release  : 22
URL      : https://bitbucket.org/eigen/eigen/get/3.3.7.tar.bz2
Source0  : https://bitbucket.org/eigen/eigen/get/3.3.7.tar.bz2
Summary  : A C++ template library for linear algebra: vectors, matrices, and related algorithms
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Attribution GPL-2.0 GPL-3.0 LGPL-2.1 MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: eigen-data = %{version}-%{release}
Requires: eigen-license = %{version}-%{release}
BuildRequires : SuiteSparse-dev
BuildRequires : beignet-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : fftw-dev
BuildRequires : freeglut-dev
BuildRequires : glew-dev
BuildRequires : glibc-dev
BuildRequires : glu-dev
BuildRequires : gmp-dev
BuildRequires : mesa-dev
BuildRequires : mpfr-dev
BuildRequires : openblas
BuildRequires : openmpi-dev
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : python3

%description
Navigation:
left button:           rotate around the target
middle button:         zoom
left button + ctrl     quake rotate (rotate around camera position)
middle button + ctrl   walk (progress along camera's z direction)
left button:           pan (translate in the XY camera's plane)

%package data
Summary: data components for the eigen package.
Group: Data

%description data
data components for the eigen package.


%package dev
Summary: dev components for the eigen package.
Group: Development
Requires: eigen-data = %{version}-%{release}
Provides: eigen-devel = %{version}-%{release}

%description dev
dev components for the eigen package.


%package license
Summary: license components for the eigen package.
Group: Default

%description license
license components for the eigen package.


%prep
%setup -q -n eigen-eigen-323c052e1731

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1544709520
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1544709520
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/eigen
cp COPYING.BSD %{buildroot}/usr/share/package-licenses/eigen/COPYING.BSD
cp COPYING.GPL %{buildroot}/usr/share/package-licenses/eigen/COPYING.GPL
cp COPYING.LGPL %{buildroot}/usr/share/package-licenses/eigen/COPYING.LGPL
cp COPYING.MINPACK %{buildroot}/usr/share/package-licenses/eigen/COPYING.MINPACK
cp COPYING.MPL2 %{buildroot}/usr/share/package-licenses/eigen/COPYING.MPL2
cp COPYING.README %{buildroot}/usr/share/package-licenses/eigen/COPYING.README
cp bench/btl/COPYING %{buildroot}/usr/share/package-licenses/eigen/bench_btl_COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/eigen3/cmake/Eigen3Config.cmake
/usr/share/eigen3/cmake/Eigen3ConfigVersion.cmake
/usr/share/eigen3/cmake/Eigen3Targets.cmake
/usr/share/eigen3/cmake/UseEigen3.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/eigen3/Eigen/Cholesky
/usr/include/eigen3/Eigen/CholmodSupport
/usr/include/eigen3/Eigen/Core
/usr/include/eigen3/Eigen/Dense
/usr/include/eigen3/Eigen/Eigen
/usr/include/eigen3/Eigen/Eigenvalues
/usr/include/eigen3/Eigen/Geometry
/usr/include/eigen3/Eigen/Householder
/usr/include/eigen3/Eigen/IterativeLinearSolvers
/usr/include/eigen3/Eigen/Jacobi
/usr/include/eigen3/Eigen/LU
/usr/include/eigen3/Eigen/MetisSupport
/usr/include/eigen3/Eigen/OrderingMethods
/usr/include/eigen3/Eigen/PaStiXSupport
/usr/include/eigen3/Eigen/PardisoSupport
/usr/include/eigen3/Eigen/QR
/usr/include/eigen3/Eigen/QtAlignedMalloc
/usr/include/eigen3/Eigen/SPQRSupport
/usr/include/eigen3/Eigen/SVD
/usr/include/eigen3/Eigen/Sparse
/usr/include/eigen3/Eigen/SparseCholesky
/usr/include/eigen3/Eigen/SparseCore
/usr/include/eigen3/Eigen/SparseLU
/usr/include/eigen3/Eigen/SparseQR
/usr/include/eigen3/Eigen/StdDeque
/usr/include/eigen3/Eigen/StdList
/usr/include/eigen3/Eigen/StdVector
/usr/include/eigen3/Eigen/SuperLUSupport
/usr/include/eigen3/Eigen/UmfPackSupport
/usr/include/eigen3/Eigen/src/Cholesky/LDLT.h
/usr/include/eigen3/Eigen/src/Cholesky/LLT.h
/usr/include/eigen3/Eigen/src/Cholesky/LLT_LAPACKE.h
/usr/include/eigen3/Eigen/src/CholmodSupport/CholmodSupport.h
/usr/include/eigen3/Eigen/src/Core/Array.h
/usr/include/eigen3/Eigen/src/Core/ArrayBase.h
/usr/include/eigen3/Eigen/src/Core/ArrayWrapper.h
/usr/include/eigen3/Eigen/src/Core/Assign.h
/usr/include/eigen3/Eigen/src/Core/AssignEvaluator.h
/usr/include/eigen3/Eigen/src/Core/Assign_MKL.h
/usr/include/eigen3/Eigen/src/Core/BandMatrix.h
/usr/include/eigen3/Eigen/src/Core/Block.h
/usr/include/eigen3/Eigen/src/Core/BooleanRedux.h
/usr/include/eigen3/Eigen/src/Core/CommaInitializer.h
/usr/include/eigen3/Eigen/src/Core/ConditionEstimator.h
/usr/include/eigen3/Eigen/src/Core/CoreEvaluators.h
/usr/include/eigen3/Eigen/src/Core/CoreIterators.h
/usr/include/eigen3/Eigen/src/Core/CwiseBinaryOp.h
/usr/include/eigen3/Eigen/src/Core/CwiseNullaryOp.h
/usr/include/eigen3/Eigen/src/Core/CwiseTernaryOp.h
/usr/include/eigen3/Eigen/src/Core/CwiseUnaryOp.h
/usr/include/eigen3/Eigen/src/Core/CwiseUnaryView.h
/usr/include/eigen3/Eigen/src/Core/DenseBase.h
/usr/include/eigen3/Eigen/src/Core/DenseCoeffsBase.h
/usr/include/eigen3/Eigen/src/Core/DenseStorage.h
/usr/include/eigen3/Eigen/src/Core/Diagonal.h
/usr/include/eigen3/Eigen/src/Core/DiagonalMatrix.h
/usr/include/eigen3/Eigen/src/Core/DiagonalProduct.h
/usr/include/eigen3/Eigen/src/Core/Dot.h
/usr/include/eigen3/Eigen/src/Core/EigenBase.h
/usr/include/eigen3/Eigen/src/Core/ForceAlignedAccess.h
/usr/include/eigen3/Eigen/src/Core/Fuzzy.h
/usr/include/eigen3/Eigen/src/Core/GeneralProduct.h
/usr/include/eigen3/Eigen/src/Core/GenericPacketMath.h
/usr/include/eigen3/Eigen/src/Core/GlobalFunctions.h
/usr/include/eigen3/Eigen/src/Core/IO.h
/usr/include/eigen3/Eigen/src/Core/Inverse.h
/usr/include/eigen3/Eigen/src/Core/Map.h
/usr/include/eigen3/Eigen/src/Core/MapBase.h
/usr/include/eigen3/Eigen/src/Core/MathFunctions.h
/usr/include/eigen3/Eigen/src/Core/MathFunctionsImpl.h
/usr/include/eigen3/Eigen/src/Core/Matrix.h
/usr/include/eigen3/Eigen/src/Core/MatrixBase.h
/usr/include/eigen3/Eigen/src/Core/NestByValue.h
/usr/include/eigen3/Eigen/src/Core/NoAlias.h
/usr/include/eigen3/Eigen/src/Core/NumTraits.h
/usr/include/eigen3/Eigen/src/Core/PermutationMatrix.h
/usr/include/eigen3/Eigen/src/Core/PlainObjectBase.h
/usr/include/eigen3/Eigen/src/Core/Product.h
/usr/include/eigen3/Eigen/src/Core/ProductEvaluators.h
/usr/include/eigen3/Eigen/src/Core/Random.h
/usr/include/eigen3/Eigen/src/Core/Redux.h
/usr/include/eigen3/Eigen/src/Core/Ref.h
/usr/include/eigen3/Eigen/src/Core/Replicate.h
/usr/include/eigen3/Eigen/src/Core/ReturnByValue.h
/usr/include/eigen3/Eigen/src/Core/Reverse.h
/usr/include/eigen3/Eigen/src/Core/Select.h
/usr/include/eigen3/Eigen/src/Core/SelfAdjointView.h
/usr/include/eigen3/Eigen/src/Core/SelfCwiseBinaryOp.h
/usr/include/eigen3/Eigen/src/Core/Solve.h
/usr/include/eigen3/Eigen/src/Core/SolveTriangular.h
/usr/include/eigen3/Eigen/src/Core/SolverBase.h
/usr/include/eigen3/Eigen/src/Core/StableNorm.h
/usr/include/eigen3/Eigen/src/Core/Stride.h
/usr/include/eigen3/Eigen/src/Core/Swap.h
/usr/include/eigen3/Eigen/src/Core/Transpose.h
/usr/include/eigen3/Eigen/src/Core/Transpositions.h
/usr/include/eigen3/Eigen/src/Core/TriangularMatrix.h
/usr/include/eigen3/Eigen/src/Core/VectorBlock.h
/usr/include/eigen3/Eigen/src/Core/VectorwiseOp.h
/usr/include/eigen3/Eigen/src/Core/Visitor.h
/usr/include/eigen3/Eigen/src/Core/arch/AVX/Complex.h
/usr/include/eigen3/Eigen/src/Core/arch/AVX/MathFunctions.h
/usr/include/eigen3/Eigen/src/Core/arch/AVX/PacketMath.h
/usr/include/eigen3/Eigen/src/Core/arch/AVX/TypeCasting.h
/usr/include/eigen3/Eigen/src/Core/arch/AVX512/MathFunctions.h
/usr/include/eigen3/Eigen/src/Core/arch/AVX512/PacketMath.h
/usr/include/eigen3/Eigen/src/Core/arch/AltiVec/Complex.h
/usr/include/eigen3/Eigen/src/Core/arch/AltiVec/MathFunctions.h
/usr/include/eigen3/Eigen/src/Core/arch/AltiVec/PacketMath.h
/usr/include/eigen3/Eigen/src/Core/arch/CUDA/Complex.h
/usr/include/eigen3/Eigen/src/Core/arch/CUDA/Half.h
/usr/include/eigen3/Eigen/src/Core/arch/CUDA/MathFunctions.h
/usr/include/eigen3/Eigen/src/Core/arch/CUDA/PacketMath.h
/usr/include/eigen3/Eigen/src/Core/arch/CUDA/PacketMathHalf.h
/usr/include/eigen3/Eigen/src/Core/arch/CUDA/TypeCasting.h
/usr/include/eigen3/Eigen/src/Core/arch/Default/ConjHelper.h
/usr/include/eigen3/Eigen/src/Core/arch/Default/Settings.h
/usr/include/eigen3/Eigen/src/Core/arch/NEON/Complex.h
/usr/include/eigen3/Eigen/src/Core/arch/NEON/MathFunctions.h
/usr/include/eigen3/Eigen/src/Core/arch/NEON/PacketMath.h
/usr/include/eigen3/Eigen/src/Core/arch/SSE/Complex.h
/usr/include/eigen3/Eigen/src/Core/arch/SSE/MathFunctions.h
/usr/include/eigen3/Eigen/src/Core/arch/SSE/PacketMath.h
/usr/include/eigen3/Eigen/src/Core/arch/SSE/TypeCasting.h
/usr/include/eigen3/Eigen/src/Core/arch/ZVector/Complex.h
/usr/include/eigen3/Eigen/src/Core/arch/ZVector/MathFunctions.h
/usr/include/eigen3/Eigen/src/Core/arch/ZVector/PacketMath.h
/usr/include/eigen3/Eigen/src/Core/functors/AssignmentFunctors.h
/usr/include/eigen3/Eigen/src/Core/functors/BinaryFunctors.h
/usr/include/eigen3/Eigen/src/Core/functors/NullaryFunctors.h
/usr/include/eigen3/Eigen/src/Core/functors/StlFunctors.h
/usr/include/eigen3/Eigen/src/Core/functors/TernaryFunctors.h
/usr/include/eigen3/Eigen/src/Core/functors/UnaryFunctors.h
/usr/include/eigen3/Eigen/src/Core/products/GeneralBlockPanelKernel.h
/usr/include/eigen3/Eigen/src/Core/products/GeneralMatrixMatrix.h
/usr/include/eigen3/Eigen/src/Core/products/GeneralMatrixMatrixTriangular.h
/usr/include/eigen3/Eigen/src/Core/products/GeneralMatrixMatrixTriangular_BLAS.h
/usr/include/eigen3/Eigen/src/Core/products/GeneralMatrixMatrix_BLAS.h
/usr/include/eigen3/Eigen/src/Core/products/GeneralMatrixVector.h
/usr/include/eigen3/Eigen/src/Core/products/GeneralMatrixVector_BLAS.h
/usr/include/eigen3/Eigen/src/Core/products/Parallelizer.h
/usr/include/eigen3/Eigen/src/Core/products/SelfadjointMatrixMatrix.h
/usr/include/eigen3/Eigen/src/Core/products/SelfadjointMatrixMatrix_BLAS.h
/usr/include/eigen3/Eigen/src/Core/products/SelfadjointMatrixVector.h
/usr/include/eigen3/Eigen/src/Core/products/SelfadjointMatrixVector_BLAS.h
/usr/include/eigen3/Eigen/src/Core/products/SelfadjointProduct.h
/usr/include/eigen3/Eigen/src/Core/products/SelfadjointRank2Update.h
/usr/include/eigen3/Eigen/src/Core/products/TriangularMatrixMatrix.h
/usr/include/eigen3/Eigen/src/Core/products/TriangularMatrixMatrix_BLAS.h
/usr/include/eigen3/Eigen/src/Core/products/TriangularMatrixVector.h
/usr/include/eigen3/Eigen/src/Core/products/TriangularMatrixVector_BLAS.h
/usr/include/eigen3/Eigen/src/Core/products/TriangularSolverMatrix.h
/usr/include/eigen3/Eigen/src/Core/products/TriangularSolverMatrix_BLAS.h
/usr/include/eigen3/Eigen/src/Core/products/TriangularSolverVector.h
/usr/include/eigen3/Eigen/src/Core/util/BlasUtil.h
/usr/include/eigen3/Eigen/src/Core/util/Constants.h
/usr/include/eigen3/Eigen/src/Core/util/DisableStupidWarnings.h
/usr/include/eigen3/Eigen/src/Core/util/ForwardDeclarations.h
/usr/include/eigen3/Eigen/src/Core/util/MKL_support.h
/usr/include/eigen3/Eigen/src/Core/util/Macros.h
/usr/include/eigen3/Eigen/src/Core/util/Memory.h
/usr/include/eigen3/Eigen/src/Core/util/Meta.h
/usr/include/eigen3/Eigen/src/Core/util/NonMPL2.h
/usr/include/eigen3/Eigen/src/Core/util/ReenableStupidWarnings.h
/usr/include/eigen3/Eigen/src/Core/util/StaticAssert.h
/usr/include/eigen3/Eigen/src/Core/util/XprHelper.h
/usr/include/eigen3/Eigen/src/Eigenvalues/ComplexEigenSolver.h
/usr/include/eigen3/Eigen/src/Eigenvalues/ComplexSchur.h
/usr/include/eigen3/Eigen/src/Eigenvalues/ComplexSchur_LAPACKE.h
/usr/include/eigen3/Eigen/src/Eigenvalues/EigenSolver.h
/usr/include/eigen3/Eigen/src/Eigenvalues/GeneralizedEigenSolver.h
/usr/include/eigen3/Eigen/src/Eigenvalues/GeneralizedSelfAdjointEigenSolver.h
/usr/include/eigen3/Eigen/src/Eigenvalues/HessenbergDecomposition.h
/usr/include/eigen3/Eigen/src/Eigenvalues/MatrixBaseEigenvalues.h
/usr/include/eigen3/Eigen/src/Eigenvalues/RealQZ.h
/usr/include/eigen3/Eigen/src/Eigenvalues/RealSchur.h
/usr/include/eigen3/Eigen/src/Eigenvalues/RealSchur_LAPACKE.h
/usr/include/eigen3/Eigen/src/Eigenvalues/SelfAdjointEigenSolver.h
/usr/include/eigen3/Eigen/src/Eigenvalues/SelfAdjointEigenSolver_LAPACKE.h
/usr/include/eigen3/Eigen/src/Eigenvalues/Tridiagonalization.h
/usr/include/eigen3/Eigen/src/Geometry/AlignedBox.h
/usr/include/eigen3/Eigen/src/Geometry/AngleAxis.h
/usr/include/eigen3/Eigen/src/Geometry/EulerAngles.h
/usr/include/eigen3/Eigen/src/Geometry/Homogeneous.h
/usr/include/eigen3/Eigen/src/Geometry/Hyperplane.h
/usr/include/eigen3/Eigen/src/Geometry/OrthoMethods.h
/usr/include/eigen3/Eigen/src/Geometry/ParametrizedLine.h
/usr/include/eigen3/Eigen/src/Geometry/Quaternion.h
/usr/include/eigen3/Eigen/src/Geometry/Rotation2D.h
/usr/include/eigen3/Eigen/src/Geometry/RotationBase.h
/usr/include/eigen3/Eigen/src/Geometry/Scaling.h
/usr/include/eigen3/Eigen/src/Geometry/Transform.h
/usr/include/eigen3/Eigen/src/Geometry/Translation.h
/usr/include/eigen3/Eigen/src/Geometry/Umeyama.h
/usr/include/eigen3/Eigen/src/Geometry/arch/Geometry_SSE.h
/usr/include/eigen3/Eigen/src/Householder/BlockHouseholder.h
/usr/include/eigen3/Eigen/src/Householder/Householder.h
/usr/include/eigen3/Eigen/src/Householder/HouseholderSequence.h
/usr/include/eigen3/Eigen/src/IterativeLinearSolvers/BasicPreconditioners.h
/usr/include/eigen3/Eigen/src/IterativeLinearSolvers/BiCGSTAB.h
/usr/include/eigen3/Eigen/src/IterativeLinearSolvers/ConjugateGradient.h
/usr/include/eigen3/Eigen/src/IterativeLinearSolvers/IncompleteCholesky.h
/usr/include/eigen3/Eigen/src/IterativeLinearSolvers/IncompleteLUT.h
/usr/include/eigen3/Eigen/src/IterativeLinearSolvers/IterativeSolverBase.h
/usr/include/eigen3/Eigen/src/IterativeLinearSolvers/LeastSquareConjugateGradient.h
/usr/include/eigen3/Eigen/src/IterativeLinearSolvers/SolveWithGuess.h
/usr/include/eigen3/Eigen/src/Jacobi/Jacobi.h
/usr/include/eigen3/Eigen/src/LU/Determinant.h
/usr/include/eigen3/Eigen/src/LU/FullPivLU.h
/usr/include/eigen3/Eigen/src/LU/InverseImpl.h
/usr/include/eigen3/Eigen/src/LU/PartialPivLU.h
/usr/include/eigen3/Eigen/src/LU/PartialPivLU_LAPACKE.h
/usr/include/eigen3/Eigen/src/LU/arch/Inverse_SSE.h
/usr/include/eigen3/Eigen/src/MetisSupport/MetisSupport.h
/usr/include/eigen3/Eigen/src/OrderingMethods/Amd.h
/usr/include/eigen3/Eigen/src/OrderingMethods/Eigen_Colamd.h
/usr/include/eigen3/Eigen/src/OrderingMethods/Ordering.h
/usr/include/eigen3/Eigen/src/PaStiXSupport/PaStiXSupport.h
/usr/include/eigen3/Eigen/src/PardisoSupport/PardisoSupport.h
/usr/include/eigen3/Eigen/src/QR/ColPivHouseholderQR.h
/usr/include/eigen3/Eigen/src/QR/ColPivHouseholderQR_LAPACKE.h
/usr/include/eigen3/Eigen/src/QR/CompleteOrthogonalDecomposition.h
/usr/include/eigen3/Eigen/src/QR/FullPivHouseholderQR.h
/usr/include/eigen3/Eigen/src/QR/HouseholderQR.h
/usr/include/eigen3/Eigen/src/QR/HouseholderQR_LAPACKE.h
/usr/include/eigen3/Eigen/src/SPQRSupport/SuiteSparseQRSupport.h
/usr/include/eigen3/Eigen/src/SVD/BDCSVD.h
/usr/include/eigen3/Eigen/src/SVD/JacobiSVD.h
/usr/include/eigen3/Eigen/src/SVD/JacobiSVD_LAPACKE.h
/usr/include/eigen3/Eigen/src/SVD/SVDBase.h
/usr/include/eigen3/Eigen/src/SVD/UpperBidiagonalization.h
/usr/include/eigen3/Eigen/src/SparseCholesky/SimplicialCholesky.h
/usr/include/eigen3/Eigen/src/SparseCholesky/SimplicialCholesky_impl.h
/usr/include/eigen3/Eigen/src/SparseCore/AmbiVector.h
/usr/include/eigen3/Eigen/src/SparseCore/CompressedStorage.h
/usr/include/eigen3/Eigen/src/SparseCore/ConservativeSparseSparseProduct.h
/usr/include/eigen3/Eigen/src/SparseCore/MappedSparseMatrix.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseAssign.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseBlock.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseColEtree.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseCompressedBase.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseCwiseBinaryOp.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseCwiseUnaryOp.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseDenseProduct.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseDiagonalProduct.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseDot.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseFuzzy.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseMap.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseMatrix.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseMatrixBase.h
/usr/include/eigen3/Eigen/src/SparseCore/SparsePermutation.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseProduct.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseRedux.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseRef.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseSelfAdjointView.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseSolverBase.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseSparseProductWithPruning.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseTranspose.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseTriangularView.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseUtil.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseVector.h
/usr/include/eigen3/Eigen/src/SparseCore/SparseView.h
/usr/include/eigen3/Eigen/src/SparseCore/TriangularSolver.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLUImpl.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_Memory.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_Structs.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_SupernodalMatrix.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_Utils.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_column_bmod.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_column_dfs.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_copy_to_ucol.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_gemm_kernel.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_heap_relax_snode.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_kernel_bmod.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_panel_bmod.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_panel_dfs.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_pivotL.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_pruneL.h
/usr/include/eigen3/Eigen/src/SparseLU/SparseLU_relax_snode.h
/usr/include/eigen3/Eigen/src/SparseQR/SparseQR.h
/usr/include/eigen3/Eigen/src/StlSupport/StdDeque.h
/usr/include/eigen3/Eigen/src/StlSupport/StdList.h
/usr/include/eigen3/Eigen/src/StlSupport/StdVector.h
/usr/include/eigen3/Eigen/src/StlSupport/details.h
/usr/include/eigen3/Eigen/src/SuperLUSupport/SuperLUSupport.h
/usr/include/eigen3/Eigen/src/UmfPackSupport/UmfPackSupport.h
/usr/include/eigen3/Eigen/src/misc/Image.h
/usr/include/eigen3/Eigen/src/misc/Kernel.h
/usr/include/eigen3/Eigen/src/misc/RealSvd2x2.h
/usr/include/eigen3/Eigen/src/misc/blas.h
/usr/include/eigen3/Eigen/src/misc/lapack.h
/usr/include/eigen3/Eigen/src/misc/lapacke.h
/usr/include/eigen3/Eigen/src/misc/lapacke_mangling.h
/usr/include/eigen3/Eigen/src/plugins/ArrayCwiseBinaryOps.h
/usr/include/eigen3/Eigen/src/plugins/ArrayCwiseUnaryOps.h
/usr/include/eigen3/Eigen/src/plugins/BlockMethods.h
/usr/include/eigen3/Eigen/src/plugins/CommonCwiseBinaryOps.h
/usr/include/eigen3/Eigen/src/plugins/CommonCwiseUnaryOps.h
/usr/include/eigen3/Eigen/src/plugins/MatrixCwiseBinaryOps.h
/usr/include/eigen3/Eigen/src/plugins/MatrixCwiseUnaryOps.h
/usr/include/eigen3/signature_of_eigen3_matrix_library
/usr/include/eigen3/unsupported/Eigen/AdolcForward
/usr/include/eigen3/unsupported/Eigen/AlignedVector3
/usr/include/eigen3/unsupported/Eigen/ArpackSupport
/usr/include/eigen3/unsupported/Eigen/AutoDiff
/usr/include/eigen3/unsupported/Eigen/BVH
/usr/include/eigen3/unsupported/Eigen/CXX11/Tensor
/usr/include/eigen3/unsupported/Eigen/CXX11/TensorSymmetry
/usr/include/eigen3/unsupported/Eigen/CXX11/ThreadPool
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/Tensor.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorArgMax.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorAssign.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorBase.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorBroadcasting.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorChipping.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorConcatenation.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorContraction.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorContractionBlocking.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorContractionCuda.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorContractionMapper.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorContractionThreadPool.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorConversion.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorConvolution.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorCostModel.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorCustomOp.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorDevice.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceCuda.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceDefault.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceSycl.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorDeviceThreadPool.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorDimensionList.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorDimensions.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorEvalTo.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorEvaluator.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorExecutor.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorExpr.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorFFT.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorFixedSize.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorForcedEval.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorForwardDeclarations.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorFunctors.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorGenerator.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorGlobalFunctions.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorIO.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorImagePatch.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorIndexList.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorInflation.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorInitializer.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorIntDiv.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorLayoutSwap.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorMacros.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorMap.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorMeta.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorMorphing.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorPadding.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorPatch.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorRandom.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorReduction.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorReductionCuda.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorReductionSycl.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorRef.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorReverse.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorScan.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorShuffling.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorStorage.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorStriding.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorSycl.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorSyclConvertToDeviceExpression.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorSyclExprConstructor.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorSyclExtractAccessor.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorSyclExtractFunctors.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorSyclLeafCount.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorSyclPlaceHolderExpr.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorSyclRun.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorSyclTuple.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorTraits.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorUInt128.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/Tensor/TensorVolumePatch.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/TensorSymmetry/DynamicSymmetry.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/TensorSymmetry/StaticSymmetry.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/TensorSymmetry/Symmetry.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/TensorSymmetry/util/TemplateGroupTheory.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/ThreadPool/EventCount.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/ThreadPool/NonBlockingThreadPool.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/ThreadPool/RunQueue.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/ThreadPool/SimpleThreadPool.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/ThreadPool/ThreadEnvironment.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/ThreadPool/ThreadLocal.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/ThreadPool/ThreadPoolInterface.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/ThreadPool/ThreadYield.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/util/CXX11Meta.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/util/CXX11Workarounds.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/util/EmulateArray.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/util/EmulateCXX11Meta.h
/usr/include/eigen3/unsupported/Eigen/CXX11/src/util/MaxSizeVector.h
/usr/include/eigen3/unsupported/Eigen/EulerAngles
/usr/include/eigen3/unsupported/Eigen/FFT
/usr/include/eigen3/unsupported/Eigen/IterativeSolvers
/usr/include/eigen3/unsupported/Eigen/KroneckerProduct
/usr/include/eigen3/unsupported/Eigen/LevenbergMarquardt
/usr/include/eigen3/unsupported/Eigen/MPRealSupport
/usr/include/eigen3/unsupported/Eigen/MatrixFunctions
/usr/include/eigen3/unsupported/Eigen/MoreVectorization
/usr/include/eigen3/unsupported/Eigen/NonLinearOptimization
/usr/include/eigen3/unsupported/Eigen/NumericalDiff
/usr/include/eigen3/unsupported/Eigen/OpenGLSupport
/usr/include/eigen3/unsupported/Eigen/Polynomials
/usr/include/eigen3/unsupported/Eigen/Skyline
/usr/include/eigen3/unsupported/Eigen/SparseExtra
/usr/include/eigen3/unsupported/Eigen/SpecialFunctions
/usr/include/eigen3/unsupported/Eigen/Splines
/usr/include/eigen3/unsupported/Eigen/src/AutoDiff/AutoDiffJacobian.h
/usr/include/eigen3/unsupported/Eigen/src/AutoDiff/AutoDiffScalar.h
/usr/include/eigen3/unsupported/Eigen/src/AutoDiff/AutoDiffVector.h
/usr/include/eigen3/unsupported/Eigen/src/BVH/BVAlgorithms.h
/usr/include/eigen3/unsupported/Eigen/src/BVH/KdBVH.h
/usr/include/eigen3/unsupported/Eigen/src/Eigenvalues/ArpackSelfAdjointEigenSolver.h
/usr/include/eigen3/unsupported/Eigen/src/EulerAngles/EulerAngles.h
/usr/include/eigen3/unsupported/Eigen/src/EulerAngles/EulerSystem.h
/usr/include/eigen3/unsupported/Eigen/src/FFT/ei_fftw_impl.h
/usr/include/eigen3/unsupported/Eigen/src/FFT/ei_kissfft_impl.h
/usr/include/eigen3/unsupported/Eigen/src/IterativeSolvers/ConstrainedConjGrad.h
/usr/include/eigen3/unsupported/Eigen/src/IterativeSolvers/DGMRES.h
/usr/include/eigen3/unsupported/Eigen/src/IterativeSolvers/GMRES.h
/usr/include/eigen3/unsupported/Eigen/src/IterativeSolvers/IncompleteLU.h
/usr/include/eigen3/unsupported/Eigen/src/IterativeSolvers/IterationController.h
/usr/include/eigen3/unsupported/Eigen/src/IterativeSolvers/MINRES.h
/usr/include/eigen3/unsupported/Eigen/src/IterativeSolvers/Scaling.h
/usr/include/eigen3/unsupported/Eigen/src/KroneckerProduct/KroneckerTensorProduct.h
/usr/include/eigen3/unsupported/Eigen/src/LevenbergMarquardt/LMcovar.h
/usr/include/eigen3/unsupported/Eigen/src/LevenbergMarquardt/LMonestep.h
/usr/include/eigen3/unsupported/Eigen/src/LevenbergMarquardt/LMpar.h
/usr/include/eigen3/unsupported/Eigen/src/LevenbergMarquardt/LMqrsolv.h
/usr/include/eigen3/unsupported/Eigen/src/LevenbergMarquardt/LevenbergMarquardt.h
/usr/include/eigen3/unsupported/Eigen/src/MatrixFunctions/MatrixExponential.h
/usr/include/eigen3/unsupported/Eigen/src/MatrixFunctions/MatrixFunction.h
/usr/include/eigen3/unsupported/Eigen/src/MatrixFunctions/MatrixLogarithm.h
/usr/include/eigen3/unsupported/Eigen/src/MatrixFunctions/MatrixPower.h
/usr/include/eigen3/unsupported/Eigen/src/MatrixFunctions/MatrixSquareRoot.h
/usr/include/eigen3/unsupported/Eigen/src/MatrixFunctions/StemFunction.h
/usr/include/eigen3/unsupported/Eigen/src/MoreVectorization/MathFunctions.h
/usr/include/eigen3/unsupported/Eigen/src/NonLinearOptimization/HybridNonLinearSolver.h
/usr/include/eigen3/unsupported/Eigen/src/NonLinearOptimization/LevenbergMarquardt.h
/usr/include/eigen3/unsupported/Eigen/src/NonLinearOptimization/chkder.h
/usr/include/eigen3/unsupported/Eigen/src/NonLinearOptimization/covar.h
/usr/include/eigen3/unsupported/Eigen/src/NonLinearOptimization/dogleg.h
/usr/include/eigen3/unsupported/Eigen/src/NonLinearOptimization/fdjac1.h
/usr/include/eigen3/unsupported/Eigen/src/NonLinearOptimization/lmpar.h
/usr/include/eigen3/unsupported/Eigen/src/NonLinearOptimization/qrsolv.h
/usr/include/eigen3/unsupported/Eigen/src/NonLinearOptimization/r1mpyq.h
/usr/include/eigen3/unsupported/Eigen/src/NonLinearOptimization/r1updt.h
/usr/include/eigen3/unsupported/Eigen/src/NonLinearOptimization/rwupdt.h
/usr/include/eigen3/unsupported/Eigen/src/NumericalDiff/NumericalDiff.h
/usr/include/eigen3/unsupported/Eigen/src/Polynomials/Companion.h
/usr/include/eigen3/unsupported/Eigen/src/Polynomials/PolynomialSolver.h
/usr/include/eigen3/unsupported/Eigen/src/Polynomials/PolynomialUtils.h
/usr/include/eigen3/unsupported/Eigen/src/Skyline/SkylineInplaceLU.h
/usr/include/eigen3/unsupported/Eigen/src/Skyline/SkylineMatrix.h
/usr/include/eigen3/unsupported/Eigen/src/Skyline/SkylineMatrixBase.h
/usr/include/eigen3/unsupported/Eigen/src/Skyline/SkylineProduct.h
/usr/include/eigen3/unsupported/Eigen/src/Skyline/SkylineStorage.h
/usr/include/eigen3/unsupported/Eigen/src/Skyline/SkylineUtil.h
/usr/include/eigen3/unsupported/Eigen/src/SparseExtra/BlockOfDynamicSparseMatrix.h
/usr/include/eigen3/unsupported/Eigen/src/SparseExtra/BlockSparseMatrix.h
/usr/include/eigen3/unsupported/Eigen/src/SparseExtra/DynamicSparseMatrix.h
/usr/include/eigen3/unsupported/Eigen/src/SparseExtra/MarketIO.h
/usr/include/eigen3/unsupported/Eigen/src/SparseExtra/MatrixMarketIterator.h
/usr/include/eigen3/unsupported/Eigen/src/SparseExtra/RandomSetter.h
/usr/include/eigen3/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsArrayAPI.h
/usr/include/eigen3/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsFunctors.h
/usr/include/eigen3/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsHalf.h
/usr/include/eigen3/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsImpl.h
/usr/include/eigen3/unsupported/Eigen/src/SpecialFunctions/SpecialFunctionsPacketMath.h
/usr/include/eigen3/unsupported/Eigen/src/SpecialFunctions/arch/CUDA/CudaSpecialFunctions.h
/usr/include/eigen3/unsupported/Eigen/src/Splines/Spline.h
/usr/include/eigen3/unsupported/Eigen/src/Splines/SplineFitting.h
/usr/include/eigen3/unsupported/Eigen/src/Splines/SplineFwd.h
/usr/lib64/pkgconfig/eigen3.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/eigen/COPYING.BSD
/usr/share/package-licenses/eigen/COPYING.GPL
/usr/share/package-licenses/eigen/COPYING.LGPL
/usr/share/package-licenses/eigen/COPYING.MINPACK
/usr/share/package-licenses/eigen/COPYING.MPL2
/usr/share/package-licenses/eigen/COPYING.README
/usr/share/package-licenses/eigen/bench_btl_COPYING
