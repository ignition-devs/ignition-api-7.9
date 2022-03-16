# Changelog

All notable changes to this project will be documented in this file.

## [7.9.19] - 2022-03-16

### CI

- fix pypi upload workflow (#3) ([b870c17](https://github.com/ignition-api/7.9/commit/b870c1732f80baa0740ad730238c66044ec1bbf5))

### Documentation

- update downloads badge ([fb667d8](https://github.com/ignition-api/7.9/commit/fb667d80ec4933602762289709a0f9620ac0d413))
- remove license badge ([ade39bf](https://github.com/ignition-api/7.9/commit/ade39bfdc3e6f8118cf35a0dfe485c680d42bd7f))

### Miscellaneous Tasks

- cleanup `.pylintrc` ([49b806d](https://github.com/ignition-api/7.9/commit/49b806d2c3f5784c787ed0b4e44154bf31baff5b))
- move project to github org ([e2027c6](https://github.com/ignition-api/7.9/commit/e2027c62bd305ba0e72a27f7c0e0f6b706d71f5c))

### Refactor

- Sourcery refactored main branch (#1) ([b32da16](https://github.com/ignition-api/7.9/commit/b32da1684291097711daa2b1955d8393c07169ce))

### Styling

- format `pyproject.toml` with `pyproject-fmt` ([164f2a7](https://github.com/ignition-api/7.9/commit/164f2a749eda9d8af95e1aca73a9e88954ab7e90))

### Build

- update black from 21.12b0 to 22.1.0 ([b3fe791](https://github.com/ignition-api/7.9/commit/b3fe7915e3b94acb1fd3c3a58c76027f3cc3fbb5))
- add `sort-all@v1.2.0` ([4db4949](https://github.com/ignition-api/7.9/commit/4db4949e43fb624dd03460eafc51c9ab90340b24))

## [7.9.18.post7] - 2022-01-21

### Miscellaneous Tasks

- add `cliff.toml` file for changelog generation ([f77ca45](https://github.com/ignition-api/7.9/commit/f77ca4594109298509921009c0adc264aafe3f74))
- format setup.cfg file ([3f920ba](https://github.com/ignition-api/7.9/commit/3f920ba7e1371210c0a07b278082ee8bf9476351))
- update `.pylintrc`; remove `unused-import` ([3250737](https://github.com/ignition-api/7.9/commit/3250737ffde1d1337cd3a4eaf480c7ab25b2c2d2))

### Refactor

- define ColType as a type alias ([af8c5ca](https://github.com/ignition-api/7.9/commit/af8c5cafc7c3863e01d715a111e51c96c2091863))
- move `String` alias to `java.util` ([c94b517](https://github.com/ignition-api/7.9/commit/c94b517f996f6907c6df88cc87dfcba4e4e5681a))

### Styling

- tell `isort` to sort using Python 2.7 ([e80b077](https://github.com/ignition-api/7.9/commit/e80b077eb99c11ffde5c69747eea902b721925aa))

### Build

- update black from 21.11b1 to 21.12b0 ([9a07cb3](https://github.com/ignition-api/7.9/commit/9a07cb39e648843145bead9ae4d694a8b83b444d))
- remove files from `MANIFEST.in` ([3c36147](https://github.com/ignition-api/7.9/commit/3c36147a5c111d17f97454e1f6698c80e6ce9671))

### Revert

- undo `java.lang.String` ([75d3bb8](https://github.com/ignition-api/7.9/commit/75d3bb8da5926e6200031d8bf40d54cec7e08c27))

## [7.9.18.post6] - 2021-11-30

### Bug Fixes

- add `String` type definition ([a3cae41](https://github.com/ignition-api/7.9/commit/a3cae41bfda6850c36d7ae23ec8e35827b545f1f))

### Miscellaneous Tasks

- apply `sort-all` fixes ([f7491b0](https://github.com/ignition-api/7.9/commit/f7491b0755882e8ce861113f0ce45b5e0c3c906e))
- release 7.9.18.post6 ([96b62e7](https://github.com/ignition-api/7.9/commit/96b62e7766d2e409013308183b85161a6a4b8157))

### Build

- update `pydocstyle` hook ([11b9b23](https://github.com/ignition-api/7.9/commit/11b9b2350b9c86515986cf15e57355808dba3741))

## [7.9.18.post5] - 2021-11-29

### Features

- add `String` type ([b0f9d2b](https://github.com/ignition-api/7.9/commit/b0f9d2b5133070e62ac1e15f503cab6e2157dc9a))

### Miscellaneous Tasks

- :see_no_evil: ignore `.jython_cache` directory ([b1b989d](https://github.com/ignition-api/7.9/commit/b1b989da7f3ff26f55a185cc6141fd0bcd845d1b))
- release 7.9.18.post5 ([7679352](https://github.com/ignition-api/7.9/commit/76793525ac2a4979c72f5d658be7670009ee92b9))

### Build

- update `.pylintrc` ([00cd0a4](https://github.com/ignition-api/7.9/commit/00cd0a4a09fb2d89a46504420efa36ae46edecf3))

## [7.9.18.post4] - 2021-11-26

### Bug Fixes

- install now requires typing ([776b7e6](https://github.com/ignition-api/7.9/commit/776b7e6caac441910013a5988de5d31e23568ca5))

### Miscellaneous Tasks

- release 7.9.18.post4 ([cdb5fe4](https://github.com/ignition-api/7.9/commit/cdb5fe4e5282c2c701a8a02344ebb3b32559b2fc))

## [7.9.18.post3] - 2021-11-23

### Bug Fixes

- set `python-version` to 3.10.0 ([4eff3a0](https://github.com/ignition-api/7.9/commit/4eff3a0e6f60d828824a37dbf33d2e30e40806bd))
- set `python-version` to '3.10' ([c58c394](https://github.com/ignition-api/7.9/commit/c58c3942b1a9d29184279f7114719e345be6e531))

### CI

- update PyPI upload workflow ([82cb4c5](https://github.com/ignition-api/7.9/commit/82cb4c56a6900de4f302049563fbada5c407fa5b))
- use Python 2.7 for PyPI workflow ([35403d1](https://github.com/ignition-api/7.9/commit/35403d1e0680b354e4552476353a064c9a077e01))
- switch to Python 3.10 ([39c172f](https://github.com/ignition-api/7.9/commit/39c172f569d3a581cad4b20168127b817be9ba99))

### Documentation

- fix markdownlint errors ([ef78dec](https://github.com/ignition-api/7.9/commit/ef78decd2495fd83de037ae35d4180e8fdb002d2))

### Features

- improve `date.format` ([45cb322](https://github.com/ignition-api/7.9/commit/45cb3227aa6daf736ab1d438f5687ae3e2b91df4))
- the triumphant return of `print_function` ([468d1f9](https://github.com/ignition-api/7.9/commit/468d1f92f865e3ed80e2dd190bc1e7b726a0ef9c))
  - **BREAKING**: Python versions below 2.7.18 are no longer supported
- remove deprecated functions ([5fba371](https://github.com/ignition-api/7.9/commit/5fba37109b94a71c48c5cf0704830f6507043ab9))
  - **BREAKING**: `export*` functions have been deprecated in favor
of `system.dataset.export*` functions
- add type hints on all `system` functions ([001ea23](https://github.com/ignition-api/7.9/commit/001ea23f775d9d3bb449e09724dccae08f29b154))
  - **BREAKING**: Python versions below 2.7.18 are no longer supported

### Miscellaneous Tasks

- mirror changes from main ([031c66e](https://github.com/ignition-api/7.9/commit/031c66ec16d36bf559621c126d43902e23ac25cd))
- :see_no_evil: update .gitignore file ([95338f4](https://github.com/ignition-api/7.9/commit/95338f4687c2e947a3efc6ea2b1d2e2af9fc191f))

### Refactor

- implement informal interfaces ([3fddb8c](https://github.com/ignition-api/7.9/commit/3fddb8ccd9f0de2e2d28bf4b21a840144c91a040))

### Buil

- add `build-system` settings ([0db599a](https://github.com/ignition-api/7.9/commit/0db599a30a13c78c99d8c99939eac0445c21def8))

### Build

- update pylintrc ([d7765b5](https://github.com/ignition-api/7.9/commit/d7765b5aa3fbf6893202e26351cc5673def0ef0c))
- pre-commit autoupdate ([e0c4c27](https://github.com/ignition-api/7.9/commit/e0c4c2785d501e280a12d83e4b2212d195a29217))
- pre-commit autoupdate ([dc91907](https://github.com/ignition-api/7.9/commit/dc91907fa33ee92587e2391015d3195b75ea3856))
- deprecate Python 2.7 ([6f0b218](https://github.com/ignition-api/7.9/commit/6f0b21819a98a45fdf6cf8ab6cfc9dbfd97f1a46))
- pre-commit autoupdate ([abff7c0](https://github.com/ignition-api/7.9/commit/abff7c06680e7e63588bbb746b3df079482cda67))
- pre-commit autoupdate ([74acab1](https://github.com/ignition-api/7.9/commit/74acab1bd3003152e28ba24e363569caefe53b38))
- switch to static metadata ([a682cc8](https://github.com/ignition-api/7.9/commit/a682cc8cd3a2cae214d4cb41e543c809dc2cded9))
- update ignored files/directories ([5027caa](https://github.com/ignition-api/7.9/commit/5027caa9194a604d8f0d5b92b97cc49246f6d006))
- pre-commit autoupdate ([18ae0e6](https://github.com/ignition-api/7.9/commit/18ae0e6ef43ce0dd9637602aca9a0b2b4cab60ce))

## [7.9.18.post2] - 2021-09-21

### Features

- make PyDataSet iterable ([1c8c737](https://github.com/ignition-api/7.9/commit/1c8c737791d96f0786bdd63949e1256145f7cf8c))

## [7.9.18.post1] - 2021-09-20

### CI

- disable consider-using-f-string ([213bf54](https://github.com/ignition-api/7.9/commit/213bf546765fdd95777824cbe57ca9540a28597e))

### Documentation

- update Python version ([135a60b](https://github.com/ignition-api/7.9/commit/135a60b6db1f6d923b0c14588c3b91b021269bf9))

### Features

- add setup.py ([9b1231c](https://github.com/ignition-api/7.9/commit/9b1231c9a6927c34a062a033fcb97949d6a8b1c4))
- allow installation on 2.5, 2.6, and 2.7 ([b412539](https://github.com/ignition-api/7.9/commit/b412539b90dd9b1fc20266b618da5596d42e2b3b))
- add `com` package to `pip` release ([40bc4ae](https://github.com/ignition-api/7.9/commit/40bc4aea7d36708cde4e517552a523c2d179e7be))

### Refactor

- add pylint ([d011959](https://github.com/ignition-api/7.9/commit/d011959373cf0b93643ee35c787d3ebbddcb9c56))
  - **BREAKING**: Since Ignition 7.9 relies on Jython 2.5.3, this
  project was adapted to conform with Python 2.5.6

  Replace `from __future__ import print_function` with `import pprint`
  Add `from __future__ import with_statement` where required
  Remove features not available in Python 2.5
- allow any import level for winsound ([9a8ebdf](https://github.com/ignition-api/7.9/commit/9a8ebdfe160a589390fbbab0497965c0ca3dab90))
- add `com` package ([cb560d8](https://github.com/ignition-api/7.9/commit/cb560d89c387f51ba82828cc9878c34e1bfb3329))
- use pprint instead of print ([9affae0](https://github.com/ignition-api/7.9/commit/9affae0d4b6c088d6eb0a520fb6d84a227686e3e))

### Styling

- fix pylint found errors ([3f72e72](https://github.com/ignition-api/7.9/commit/3f72e7224997e4ecab843012ee5f33efcb42749d))

### Build

- pre-commit autoupdate ([6748c8a](https://github.com/ignition-api/7.9/commit/6748c8ab260271888b8a9022a9e739b7892dca5c))
- update black from 21.6b0 to 21.7b0 ([fd9d4c2](https://github.com/ignition-api/7.9/commit/fd9d4c253211d7cc2a0c647187bcc5541a95c3ba))
- pre-commit autoupdate ([6395266](https://github.com/ignition-api/7.9/commit/63952666075c6346838edbf97676da77e4667732))
- pre-commit autoupdate ([4e38db3](https://github.com/ignition-api/7.9/commit/4e38db350942981e866894a743e3082bfaa39e0a))
- add pylint workflow ([fec6797](https://github.com/ignition-api/7.9/commit/fec679737b60b880fc03c2b8451c74d8431d772d))
- exclude setup.py ([c82562c](https://github.com/ignition-api/7.9/commit/c82562c8f5a42ea55403619b7a35c688222b60e8))
- skip pylint ([8c8f4b1](https://github.com/ignition-api/7.9/commit/8c8f4b1713b0d7d3fcad38563c0dd8a7cead79a8))
- pre-commit autoupdate ([549c5a2](https://github.com/ignition-api/7.9/commit/549c5a27e7ae12320b19d2af2354badd74348f75))

## [7.9.18] - 2021-07-08

### Documentation

- update the copyright notice date ([031b99c](https://github.com/ignition-api/7.9/commit/031b99cb76531b9cc129fe238aefda0e5df8031d))
- update README.md ([eeec87a](https://github.com/ignition-api/7.9/commit/eeec87a28f84b6d8204570399ca346b78bdcfacb))
- update README.md ([cfe6325](https://github.com/ignition-api/7.9/commit/cfe6325d11379976931d81a38e941f32675ee1d6))
- replaced datetime for Date ([7fd70f9](https://github.com/ignition-api/7.9/commit/7fd70f977deb825756c913bb1299fba3e6ec1b81))

### Features

- bump flake8 to 3.9.1 ([6325547](https://github.com/ignition-api/7.9/commit/63255472b1d04d69a61cbf5e36715e0d5fa4ed54))
- update black 20.8b1 -> 21.4b0 ([65135f0](https://github.com/ignition-api/7.9/commit/65135f07dc70b7d04b5fca859d7a2d2080e6ae8e))
- update black 21.4b0 -> 21.4b1 ([dfba3b3](https://github.com/ignition-api/7.9/commit/dfba3b3952afedc30a8413af39178485db04df84))
- update black 21.4b1 -> 21.4b2 ([1b154a1](https://github.com/ignition-api/7.9/commit/1b154a130061a1fbe03fd618ff7a13fddfee3943))
- update black 21.4b2 -> 21.5b0 ([716dfb6](https://github.com/ignition-api/7.9/commit/716dfb6669605124a31b1a87f778ba29dcebc5e4))
- update flake8 3.9.1 -> 3.9.2 ([bf9a3c0](https://github.com/ignition-api/7.9/commit/bf9a3c0665bfb097021e731a3f5cfdc3e11f8e5b))
- update black 21.5b0 -> 21.5b1 ([5a9c6f2](https://github.com/ignition-api/7.9/commit/5a9c6f2bbd13369b1c1f574d71da5208cd3e5b27))

### Miscellaneous Tasks

- update .gitignore ([b7df19d](https://github.com/ignition-api/7.9/commit/b7df19d370f0f1fa04ab159656d1c33e2d675f28))
- update .gitignore ([5443c89](https://github.com/ignition-api/7.9/commit/5443c89b587986c8ae827bb5fbc391380fe3da9b))
- add .wakatime-project ([1902b1c](https://github.com/ignition-api/7.9/commit/1902b1cf62975ddf81eec844f87e142e7e458330))

### Refactor

- java.util.Date ([d4af597](https://github.com/ignition-api/7.9/commit/d4af597ff282363cbb4252b86138272b42970dc4))

### Styling

- :art: tell isort to use Python27 ([1e384ea](https://github.com/ignition-api/7.9/commit/1e384eabbc26aa2b9ce490d3a49ee9cbeddb67d3))
- remove blank line ([ceb9f73](https://github.com/ignition-api/7.9/commit/ceb9f73d503a1be0bbb266e0027a190b7fed4282))
- update docstrings ([679acbc](https://github.com/ignition-api/7.9/commit/679acbcc6a8e59eafeb2d5cdf39c6b5d3b4ff170))
- change from single quotes to double quotes ([2a21c62](https://github.com/ignition-api/7.9/commit/2a21c621510610a9673e4d658990a2dada9e1b46))

### Build

- bump flake8 and isort to latest version ([f3c62cf](https://github.com/ignition-api/7.9/commit/f3c62cfb42ad32022214ead919d43d74281efbbe))
- rearrange hooks ([19525e5](https://github.com/ignition-api/7.9/commit/19525e5e338d54b1971db5664ec7b868db440bc1))
- add pydocstyle hook ([0891484](https://github.com/ignition-api/7.9/commit/0891484a5d6eb100c19a7d144196c2908678486c))
- remove D209 from ignored codes ([853cef5](https://github.com/ignition-api/7.9/commit/853cef5efc0ee9af127cc48b53d5392c1c054952))
- remove E211 and E99 from ignore ([fdf0593](https://github.com/ignition-api/7.9/commit/fdf0593ddb9fcd9b9e74a3831d3ed9f90d89c59c))
- remove W503 from ignore ([01e6176](https://github.com/ignition-api/7.9/commit/01e61762a242c2cd23a174891d38349c961d0f27))
- update black 21.5b1 → 21.5b2 ([6be0041](https://github.com/ignition-api/7.9/commit/6be00416eb607042835c1836b17e6d615c0fda28))
- pre-commit autoupdate ([690c569](https://github.com/ignition-api/7.9/commit/690c569f470c22a7b4166fcd4dcc332f1255cb56))
- pre-commit autoupdate ([14fec8d](https://github.com/ignition-api/7.9/commit/14fec8d426cea673aa882a97b3bbd8a4b66596c1))
- check max complexity ([fc3d199](https://github.com/ignition-api/7.9/commit/fc3d1997766404634fdbdb54019de4ccd3e1fe10))

## [7.9.17] - 2021-02-13

### Features

- add flake8 to pre-commit hooks ([67fca3a](https://github.com/ignition-api/7.9/commit/67fca3a0ab8f5188a42f20e6306a72364b212078))

### Miscellaneous Tasks

- modify .py files permission ([1ba1988](https://github.com/ignition-api/7.9/commit/1ba19889f03ecb28e9a7a79233b80640a783d32a))
- add targeted Ignition version ([36d5435](https://github.com/ignition-api/7.9/commit/36d5435d9b84f2293ed34a564d695b9d908be168))

### Styling

- Black ([0bcc515](https://github.com/ignition-api/7.9/commit/0bcc51594791e05fbfe1ff806b8f797218daa7ef))
- flake8, isort ([27ecd6e](https://github.com/ignition-api/7.9/commit/27ecd6ee1297e476160c7fa307878306ec323f72))
- add flake8 and isort badges ([2fc085d](https://github.com/ignition-api/7.9/commit/2fc085d92c798cab21e883b00122cfe23a2a7c5d))
- :art: make isort compatible with black ([ecad888](https://github.com/ignition-api/7.9/commit/ecad888b85cf273981632a5b7f99f77624a3a80c))

## [7.9.14] - 2020-09-01

### 7.9

- Code cleanup. ([dd2daeb](https://github.com/ignition-api/7.9/commit/dd2daeb0aeac16592eee78c0e8d18358abb87f26))

### All

- Updated copyright legend. ([31c53f7](https://github.com/ignition-api/7.9/commit/31c53f7ad1f937a402cd52dd7fb0447fa508412f))

### Db

- Added getConnectionInfo and setDataSeourceEnabled. ([db6dfd6](https://github.com/ignition-api/7.9/commit/db6dfd69490d541557ca2cc15a11301ef746a331))

### File

- Fixed docstring. ([60baeed](https://github.com/ignition-api/7.9/commit/60baeed1fb0ab614b0947e8a49265c8375629ec8))

### Incendium.gui

- added warning, modified error. Added java.lang, and javax.swing packages. Opting for JOptionPane over Ignition's own errorBox and warningBox. ([ff1c03e](https://github.com/ignition-api/7.9/commit/ff1c03edae7fb1bde5c4b9bc4cd67a6e439449c3))
- Modified info method in order to use JOptionPane. ([487231e](https://github.com/ignition-api/7.9/commit/487231e922023311c949f54093556c804c722567))
- Added input function. ([0d8320a](https://github.com/ignition-api/7.9/commit/0d8320a3dab50c997c95690f1b1105b7c064d54d))

### Incendium.util

- Added get_timer ([d9b0a70](https://github.com/ignition-api/7.9/commit/d9b0a706a8d011b43511708f16a3f28d1ea0c5d0))

### Java

- Updated copyright legend. ([b7a2f31](https://github.com/ignition-api/7.9/commit/b7a2f31b137d1cff24f55d97eb213dfd94a4485e))

### Javax

- Updated copyright legend. ([ab859d3](https://github.com/ignition-api/7.9/commit/ab859d36e2000bc7f2f737a5068216073a319e4c))

### Lang

- Throwable now inherits from BaseException. ([24474c2](https://github.com/ignition-api/7.9/commit/24474c2f2cc1133d6122b3117637c39224d50372))

### System

- Updated copyright legend. ([7b4852d](https://github.com/ignition-api/7.9/commit/7b4852d0a374777ec796bbf899d29f674f77be77))

### Tag

- Update docstring. ([f5e3cbc](https://github.com/ignition-api/7.9/commit/f5e3cbc981f252b025d77916d557f83eb748f12f))
- Code clean-up. ([fb53d8e](https://github.com/ignition-api/7.9/commit/fb53d8e0f1d5a2f1bfc2fdf217311d77f781cb8e))
- Added all missing functions. ([9be6bb3](https://github.com/ignition-api/7.9/commit/9be6bb3c310e9fa98cf11bb71890643d66573eeb))
- Added optional arguments to functions and updated docstring. ([dc42ab9](https://github.com/ignition-api/7.9/commit/dc42ab946726aa3690c623f6aed2c41582994bbc))

### Util

- Added argument to winsound.MessageBeep funciton call. ([d06c492](https://github.com/ignition-api/7.9/commit/d06c492955347f2ca3b43ae7ad9ad442298c3638))

### Validate_form

- For numbers and collections we should compare to None. ([7a07ba5](https://github.com/ignition-api/7.9/commit/7a07ba5c278d40c620c189711be4a4f319858114))

<!-- generated by git-cliff -->
