#!/bin/bash

current_time=$(date "+%Y.%m.%d-%H.%M.%S")

perceval github ansible ansible \
    --category issue  \
    --tag bug  \
    --sleep-for-rate  \
    -t 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  \
    --json-line \
    --archive-path perceval_archive \
    --fetch-archive \
    -o "raw/raw_issues-$current_time" 

