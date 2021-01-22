Creating a Verilog Package
==============================

To view a few examples go to :ref:`examples` ; Feel free to fork them and play around with the projects
cd into the desired directory run the following; you will be prompted to enter your package Name, list of Authors and an optional remote URL

``$ vivp -s .   # setup``

To install dependencies : 

``$ vivp -i https://github.com/...``

To remove dependencies : 

``$ vivp -r https://github.com/...``


All dependencies are stored at `project_directory/.vpackage/repos/`
To view the list of dependencies installed and the modules they offer, use the --list or -l option

.. image:: https://github.com/AdityaNG/VIVP/blob/main/docs/img/example2.png?raw=true
    :width: 600
    :alt: Example2

To run your project, first add the list of testbench files (done only once); then --execute or -e: 

``$ vivp -add_testbench testbench.v``

``$ vivp -e``

.. image:: https://github.com/AdityaNG/VIVP/blob/main/docs/img/demo1.png?raw=true
    :width: 600
    :alt: Demo1
