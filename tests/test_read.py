'''
********************************************************************************
* Name: Read Tests
* Author: Nathan Swain
* Created On: May 16, 2013
* Copyright: (c) Brigham Young University 2013
* License: BSD 2-Clause
********************************************************************************
'''

from builtins import zip
import unittest
import os

from gsshapy.orm.file_io import *
from gsshapy.orm import ProjectFile
from gsshapy.lib import db_tools as dbt

class TestReadMethods(unittest.TestCase):
    def setUp(self):
        # Find db directory path
        here = os.path.abspath(os.path.dirname(__file__))

        # Create Test DB
        sqlalchemy_url, sql_engine = dbt.init_sqlite_memory()

        # Create DB Sessions
        self.readSession = dbt.create_session(sqlalchemy_url, sql_engine)
        self.querySession = dbt.create_session(sqlalchemy_url, sql_engine)

        # Define directory of test files to read
        self.directory = os.path.join(here, 'standard')

    def test_project_file_read(self):
        '''
        Test ProjectFile read method
        '''
        prjR, prjQ = self._read_n_query(fileIO=ProjectFile,
                                        directory=self.directory,
                                        filename='standard.prj')

        # Tests
        self.assertEqual(prjR.name, prjQ.name)
        self.assertEqual(prjR.mapType, prjQ.mapType)

        # Retrieve Cards
        cardsR = prjR.projectCards
        cardsQ = prjQ.projectCards

        for cardR, cardQ in zip(cardsR, cardsQ):
            # Compare cards and values
            self.assertEqual(cardR.name, cardQ.name)
            self.assertEqual(cardR.value, cardQ.value)

    def test_channel_input_read(self):
        '''
        Test ChannelInputFile read method
        '''
        # Read and Query
        cifR, cifQ = self._read_n_query(fileIO=ChannelInputFile,
                                        directory=self.directory,
                                        filename='standard.cif')

        # Tests
        self.assertEqual(cifR, cifQ)

        # Check Links
        linksR = cifR.streamLinks
        linksQ = cifQ.streamLinks

        for linkR, linkQ in zip(linksR, linksQ):
            self.assertEqual(linkR, linkQ)

            # Check Nodes
            nodesR = linkR.nodes
            nodesQ = linkQ.nodes

            self._list_compare(nodesR, nodesQ)

            # Check Upstream Links
            upLinksR = linkR.upstreamLinks
            upLinksQ = linkQ.upstreamLinks

            self._list_compare(upLinksR, upLinksQ)

            # Check Weirs
            weirsR = linkR.weirs
            weirsQ = linkQ.weirs

            self._list_compare(weirsR, weirsQ)

            # Check Culverts
            culvertsR = linkR.culverts
            culvertsQ = linkQ.culverts

            self._list_compare(culvertsR, culvertsQ)

            # Check Reservoir
            resR = linkR.reservoir
            resQ = linkQ.reservoir

            self.assertEqual(resR, resQ)

            # Check Reservoir Points
            if resR is not None and resQ is not None:
                resPointsR = resR.reservoirPoints
                resPointsQ = resQ.reservoirPoints
                self._list_compare(resPointsR, resPointsQ)

            # Check Trapezoidal CS
            trapR = linkR.trapezoidalCS
            trapQ = linkQ.trapezoidalCS

            self.assertEqual(trapR, trapQ)

            # Check Breakpoint CS
            breakR = linkR.breakpointCS
            breakQ = linkQ.breakpointCS

            self.assertEqual(breakR, breakQ)

            # Check Break Points
            if breakR is not None and breakQ is not None:
                bpR = breakR.breakpoints
                bpQ = breakQ.breakpoints

                self._list_compare(bpR, bpQ)

    def test_map_table_file_read(self):
        '''
        Test MapTableFile read method
        '''
        # Read and Query
        cmtR, cmtQ = self._read_n_query(fileIO=MapTableFile,
                                        directory=self.directory,
                                        filename='standard.cmt')

        # Tests

        # Check Index Maps
        idxMapsR = cmtR.indexMaps
        idxMapsQ = cmtQ.indexMaps

        self._list_compare(idxMapsR, idxMapsQ)

        # Check Map Tables
        mapTablesR = cmtR.mapTables
        mapTablesQ = cmtQ.mapTables

        for mapTableR, mapTableQ in zip(mapTablesR, mapTablesQ):
            self.assertEqual(mapTableR, mapTableQ)


            # Check sediments
            sedsR = mapTableR.sediments
            sedsQ = mapTableQ.sediments

            if sedsR is not None and sedsQ is not None:
                self._list_compare(sedsR, sedsQ)

            # Check Values
            valsR = mapTableR.values
            valsQ = mapTableQ.values

            for valR, valQ in zip(valsR, valsQ):
                self.assertEqual(valR, valQ)

                # Check Contaminant
                contamR = valR.contaminant
                contamQ = valR.contaminant


                if contamR is not None and contamQ is not None:
                    self.assertEqual(contamR, contamQ)

                # Check Index
                indexR = valR.index
                indexQ = valQ.index

                self.assertEqual(indexR, indexQ)

    def test_precip_file_read(self):
        '''
        Test PrecipFile read method
        '''
        gagR, gagQ = self._read_n_query(fileIO=PrecipFile,
                                        directory=self.directory,
                                        filename='standard.gag')

        # Tests

    def test_grid_pipe_file_read(self):
        '''
        Test GridPipeFile read method
        '''
        gpiR, gpiQ = self._read_n_query(fileIO=GridPipeFile,
                                        directory=self.directory,
                                        filename='standard.gpi')

        # Tests

    def test_grid_stream_file_read(self):
        '''
        Test GridStreamFile read method
        '''
        gstR, gstQ = self._read_n_query(fileIO=GridStreamFile,
                                        directory=self.directory,
                                        filename='standard.gst')

        # Tests

    def test_hmet_file_read(self):
        '''
        Test HmetFile read method
        '''
        hmetR, hmetQ = self._read_n_query(fileIO=HmetFile,
                                          directory=self.directory,
                                          filename='hmet_wes.hmt')

        # Tests

    def test_output_location_file_read(self):
        '''
        Test OutputLocationFile read method
        '''
        locR, locQ = self._read_n_query(fileIO=OutputLocationFile,
                                        directory=self.directory,
                                        filename='standard.ihl')

        # Tests

    def test_link_node_dataset_file_read(self):
        '''
        Test LinkNodeDatasetFile read method
        '''
        lndR, lndQ = self._read_n_query(fileIO=LinkNodeDatasetFile,
                                        directory=self.directory,
                                        filename='standard.cdp')

        # Tests

    def test_raster_map_file_read(self):
        '''
        Test RasterMapFile read method
        '''
        mapR, mapQ = self._read_n_query(fileIO=RasterMapFile,
                                        directory=self.directory,
                                        filename='standard.msk')

        # Tests

    def test_projection_file_read(self):
        '''
        Test ProjectionFile read method
        '''
        proR, proQ = self._read_n_query(fileIO=ProjectionFile,
                                        directory=self.directory,
                                        filename='standard_prj.pro')

        # Tests

    def test_replace_param_file_read(self):
        '''
        Test ReplaceParamFile read method
        '''
        repR, repQ = self._read_n_query(fileIO=ReplaceParamFile,
                                        directory=self.directory,
                                        filename='replace_param.txt')

        # Tests

    def test_replace_val_file_read(self):
        '''
        Test ReplaceValFile read method
        '''
        repR, repQ = self._read_n_query(fileIO=ReplaceValFile,
                                        directory=self.directory,
                                        filename='replace_val.txt')

        # Tests

    def test_nwsrfs_file_read(self):
        '''
        Test NwsrfsFile read method
        '''
        snwR, snwQ = self._read_n_query(fileIO=NwsrfsFile,
                                        directory=self.directory,
                                        filename='nwsrfs_elev.txt')

        # Tests

    def test_oro_gage_file_read(self):
        '''
        Test OrographicGageFile read method
        '''
        snwR, snwQ = self._read_n_query(fileIO=OrographicGageFile,
                                        directory=self.directory,
                                        filename='oro_gages.txt')

        # Tests

    def test_storm_pipe_network_file_read(self):
        '''
        Test StormPipeNetworkFile read method
        '''
        spnR, spnQ = self._read_n_query(fileIO=StormPipeNetworkFile,
                                        directory=self.directory,
                                        filename='standard.spn')

        # Tests

    def test_time_series_file_read(self):
        '''
        Test TimeSeriesFile read method
        '''
        timR, timQ = self._read_n_query(fileIO=TimeSeriesFile,
                                        directory=self.directory,
                                        filename='standard.ohl')

        # Tests
        dfR = timR.as_dataframe()
        dfQ = timQ.as_dataframe()
        assert dfR.equals(dfQ)
        assert len(dfR.index) == 10
        self.assertAlmostEqual(dfR.iloc[7, 1], 0.016869)
        self.assertAlmostEqual(dfR.index[7], 2002.42440068)

    def test_index_map_read(self):
        '''
        Test IndexMap read method
        '''
        # Instantiate GSSHAPY object for reading to database
        idxR = IndexMap(name='Soil')

        # Call read method
        idxR.read(directory=self.directory,
                  filename='Soil.idx',
                  session=self.readSession,)

        # Query from database
        idxQ = self.querySession.query(IndexMap).one()

        # Tests

    def test_project_file_read_all(self):
        '''
        Test ProjectFile read all method
        '''
        # Instantiate GSSHAPY ProjectFile object
        prjR = ProjectFile()

        # Invoke read all method
        prjR.readProject(directory=self.directory,
                         projectFileName='standard.prj',
                         session=self.readSession)

        # Query Project File
        prjQ = self.querySession.query(ProjectFile).one()

        # Tests

    def test_project_file_read_input(self):
        '''
        Test ProjectFile read input method
        '''
        # Instantiate GSSHAPY ProjectFile object
        prjR = ProjectFile()

        # Invoke read input method
        prjR.readInput(directory=self.directory,
                       projectFileName='standard.prj',
                       session=self.readSession)

        # Query Project File
        prjQ = self.querySession.query(ProjectFile).one()

        # Tests

    def test_project_file_read_output(self):
        '''
        Test ProjectFile read output method
        '''
        # Instantiate GSSHAPY ProjectFile object
        prjR = ProjectFile()

        # Invoke read output method
        prjR.readOutput(directory=self.directory,
                        projectFileName='standard.prj',
                        session=self.readSession)

        # Query Project File
        prjQ = self.querySession.query(ProjectFile).one()

        # Tests

    def _read_n_query(self, fileIO, directory, filename):
        '''
        Read to database and Query from database
        '''
        # Instantiate GSSHAPY object for reading to database
        instanceR = fileIO()

        # Call read method
        instanceR.read(directory=directory,
                       filename=filename,
                       session=self.readSession)

        # Query from database
        instanceQ = self.querySession.query(fileIO).one()

        return instanceR, instanceQ

    def _list_compare(self, listone, listtwo):
        for one, two in zip(listone, listtwo):
            self.assertEqual(one, two)

    def tearDown(self):
        self.readSession.close()
        self.querySession.close()

suite = unittest.TestLoader().loadTestsFromTestCase(TestReadMethods)

if __name__ == '__main__':
    unittest.main()
