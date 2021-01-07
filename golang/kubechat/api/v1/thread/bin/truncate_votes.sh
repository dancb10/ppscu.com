#!/usr/bin/env bash

echo "
TRUNCATE threads.thread_votes;
" | cqlsh

echo "
TRUNCATE threads.thread_votes_by_time;
" | cqlsh
