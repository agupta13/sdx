__author__ = 'arpit'

import pe_interface
import policy_handler
import params_sdx
import logging as log

log.basicConfig(filename='sdx.log',level=log.DEBUG)

members=['asA','asB','asC']


def main():
    # Start the scheduler thread.
    log.info('Starting the scheduler thread')
    schedThread = policy_handler.PQ_scheduler("sched")
    schedThread.daemon = True
    schedThread.start()

    log.info('Initialize the Rule Table')
    for ind in range(0,len(members)):
        params_sdx.RT[members[ind]]=[]
        for j in range(0,2):
            params_sdx.RT[members[ind]].append([])

    # Now start the interface for players to write their policies
    log.info('Start the interface for participants')
    pe_interface.main()


if __name__=="__main__":
    main()