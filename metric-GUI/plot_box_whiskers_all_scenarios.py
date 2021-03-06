#####################################
#
# contourf_map.py
#
#
# pass in:
#   incube - the cube to plot
#   what_am_i - th ncfile name to give a plot title
####################################

import iris
import matplotlib.pyplot as plt
import mpl_toolkits.basemap as bm
import numpy as np
import make_big_anomaly

def main(incube,outpath,what_am_i,sc,file_searcher):

    #ok, so for this plot, we want to try and make a box and whiskers plot
    # of all the models for all 4 scenarios
    # so the first thing to do is check that all 4 scenarios exist
    histcube_name = file_searcher.replace(sc,'historical')
    rcp26_name = file_searcher.replace(sc,'rcp26')
    rcp45_name = file_searcher.replace(sc, 'rcp45')
    rcp85_name = file_searcher.replace(sc, 'rcp85')
    try:
       histcube = iris.load_cube(str(histcube_name)+'_all_models.nc')
       rcp26cube = iris.load_cube(str(rcp26_name)+'_all_models.nc')
       rcp45cube = iris.load_cube(str(rcp45_name)+'_all_models.nc')
       rcp85cube = iris.load_cube(str(rcp85_name)+'_all_models.nc')
    except IOError:
	print 'One or more files do not exist. Exiting Code'
    else: 


    # Ok, so the data that is coming in is 1D. So we just need to make a box and whiskers plot
    # The data we expect in is spatially averaged with one value per year.
    # So the first thing that we need to do is collapse by year
	    plt.clf()
	    histcube = histcube.collapsed('year',iris.analysis.MEDIAN)
	    rcp26cube = rcp26cube.collapsed('year', iris.analysis.MEDIAN)
	    rcp45cube = rcp45cube.collapsed('year', iris.analysis.MEDIAN)
	    rcp85cube = rcp85cube.collapsed('year', iris.analysis.MEDIAN)
	    hist = histcube.data
            rcp26 = rcp26cube.data
	    rcp45 = rcp45cube.data
            rcp85 = rcp85cube.data
            hist = np.ndarray.tolist(hist)
	    rcp26 = np.ndarray.tolist(rcp26)
	    rcp45 = np.ndarray.tolist(rcp45)
            rcp85 = np.ndarray.tolist(rcp85)
	    data = [hist,rcp26,rcp45,rcp85]
            labels = ['hist', 'rcp2.6','rcp4.5','rcp8.5']
            plt.boxplot(data, labels = labels)
            for i in hist:
              plt.scatter(1,i, marker = '_', color = 'k')
            for i in rcp26:
              plt.scatter(2,i,marker = '_', color = 'k')
            for i in rcp45:
              plt.scatter(3,i,marker = '_', color = 'k')
            for i in rcp85:
              plt.scatter(4,i,marker = '_', color = 'k')
	    plt.savefig(str(what_am_i)+'_all_model_boxplot.png')
	    plt.show()


 
if __name__ == "__main__":
    main(incube,outpath,what_am_i)            
