
# TQCLI - TranQuant Client
TQCLI is the client application for using [TranQuant services](http://tranquant.com)

[TranQuant](http://tranquant.com) is a data marketplace that delivers real-time or batch data at a large scale from suppliers to end-users.

This client will allow you to upload and download data to and from TranQuant platform efficiently


## How to install TQCLI?

If you have pip installed:

    pip install tqcli

If you don't have pip installed:

    git clone https://github.com/Tranquant/tqcli.git
    cd tqcli
    pip install .

## How to use TQCLI?

    # 1- Create a Data Source on http://tranquant.com website
    # 2- You will see a command generated with datasource id that looks like:
    
    tqcli --datasource-id <a-datasource-id> --input <path-to-dataset-file>
    
    # 3- Go back to http://tranquant.com and view your published datasource
    # 4- You will find the dataset available under that datasource now!


If you have any questions please contact us `info@tranquant.com`

You can also join our channel: [![Gitter](https://badges.gitter.im/tqcli/Lobby.svg)](https://gitter.im/tqcli/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=body_badge)
