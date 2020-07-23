# data_envelopment_analysis

We extract data from Comma Separated Values (*.csv) files and adapt it to be used with [GLPK](https://www.gnu.org/software/glpk/). For our methodology, see the [notebooks](https://github.com/socd06/data_envelopment_analysis/tree/master/notebooks) and [scripts](https://github.com/socd06/data_envelopment_analysis/tree/master/scripts) folders.

# notebooks
## [Descriptive Statistics and Rankings](https://github.com/socd06/data_envelopment_analysis/tree/master/notebooks/statistics-and-rankings)

Several cases were proposed to prepare the data obtained by the optimization pipeline:

- a) [Clipping efficiencies to one](https://github.com/socd06/data_envelopment_analysis/tree/master/notebooks/statistics-and-rankings/clipping-over-max.ipynb).
WWTP efficiencies should be within 0-1 but some were found slightly above 1. Clipping those values to 1 would be the most practical solution to prevent having invalid values in the ranking process.

- b) [Ignoring efficiencies over one](https://github.com/socd06/data_envelopment_analysis/tree/master/notebooks/statistics-and-rankings/ignore-over-max.ipynb). This case considers values over 1 to be errors and excludes them from further analysis.

- c) [Ignore zeros](https://github.com/socd06/data_envelopment_analysis/tree/master/notebooks/statistics-and-rankings/ignore-zeros.ipynb). This case excludes zeros from further analysis.

- d) [Default case](https://github.com/socd06/data_envelopment_analysis/tree/master/notebooks/statistics-and-rankings/default.ipynb). All values given by the optimization pipeline are used to further describe and rank the WWTPs.

- e) [Clipping values over one and ignoring zeros](https://github.com/socd06/data_envelopment_analysis/tree/master/notebooks/statistics-and-rankings/clip-max-ignore-zeros.ipynb). This case clips efficiencies to 1 and excludes any row with zeros.

- f) [Ignoring values over one and zeros](https://github.com/socd06/data_envelopment_analysis/tree/master/notebooks/statistics-and-rankings/ignore-invalid.ipynb). This case excludes both efficiencies over 1 and rows with zeros.


# License
MIT License

# Original project
This project was forked from [EPonkratova's Data Envelopment Analysis](https://github.com/eponkratova/data_envelopment_analysis). See **our project** for details on our implementation.

### Data Envelopment Analysis concepts
The project was done to explore the optimiztion techniques, data envelopment analysis, in particular.

1. Data Envelopment analysis was used by Chames, Cooper and Rhodes in 1978 to evaluate educational programs for disadvantaged students but later being adopted by the private sector to measure units’ efficiency productivity.
2. Efficiency in DEA is defined as the ratio of the weighted sum of outputs of a unit to its weighted sum of inputs. A unit is deemed to be efficient if it is not possible to find a mixture of proportions of other units whose combined inputs do not exceed those of the unit being considered, but whose outputs are equal to or exceed, those of the unit. Should this not be possible, then the unit is deemed to be inefficient. Watch here, the productivity of those units which got a 100% efficiency score can be improved even further by introducing some technological changes.
3. Management can use the results of DEA to (1) locate inefficient units that require remedial management actions and do more targeted resource allocation; (2) reward the more efficient managers;(3) identify best practices to be introduced into less efficient branches; (4) set performance targets, among others.

The story behind the idea is @ https://medium.com/@eponkratova/whos-better-who-s-best-data-envelopment-analysis-a-non-mathematical-introduction-4986184f9ea3 (part 1), https://medium.com/@eponkratova/what-must-we-know-and-know-how-to-implement-and-interpret-data-envelopment-analysis-3517a6231be9 (part 2)

The interactive visualization is available @ https://eponkratova.github.io/data_envelopment_analysis/
