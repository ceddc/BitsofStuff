# coding: utf-8
import os
import arcpy


#Merge a lot of shapefiles with the same name from different subdirectories to a feature class a gdb

#basefolder
folder = "Z:\\E\\aso\\Europe_Navstreets_shp_wgs84"

#output gdb
outGdb = "Z:\\E\\aso\\Europe_Navstreets_shp_wgs84\\EuNavstreet.gdb"


# dict with shapefile name as key and array of path as value
# {'a.shp' : ['c:/dir1/a.shp','c:/dir2/a.shp','c:/dir3/a.shp']}
shapefileDic = dict()

#loop in all directories and subdirectories
for path,dirnames,filenames in os.walk(folder):
        for filename in filenames:
                if filename.endswith(".shp"):
                        #get the full path
                        fullpath =  path+'\\'+filename
                        #if not already in the dic, add it
                        if not filename in shapefileDic:
                            shapefileDic[filename] = [fullpath]
                        #if it already exist, add the new shapefile path to the array
                        else:
                             shapefileDic[filename].append(fullpath)

#we have a dic with all the shapesfiles path
#print shapefileDic

#merge them
for filename in shapefileDic:
        #we strip .shp
        featurename = filename[:-4]
        print featurename
        arcpy.Merge_management(shapefileDic[filename],outGdb+"/"+featurename)
