#!/usr/bin/env python

import sys
import os.path

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "usage: create_csv <base_path>"
        sys.exit(1)

    BASE_PATH=sys.argv[1]
    SEPARATOR=";"
    file = ""

    label = 0
    for dirname, dirnames, filenames in os.walk(BASE_PATH):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for dirname2, sessionDirs, subjectFiles in os.walk(subject_path):
                for sessionDir in sessionDirs:
                    session_path = os.path.join(subject_path, sessionDir)
                    for filename in os.listdir(session_path):
                        abs_path = "%s/%s" % (session_path, filename)
                        print "%s%s%d" % (abs_path, SEPARATOR, label)
            label += 1

