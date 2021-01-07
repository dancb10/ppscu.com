#!/usr/bin/env bash

echo "
TRUNCATE threads.threads;
" | cqlsh

echo "
TRUNCATE threads.threads_by_group;
" | cqlsh

echo "
TRUNCATE threads.threads_by_group_create_date;
" | cqlsh

echo "
TRUNCATE threads.thread_votes;
" | cqlsh

echo "
TRUNCATE threads.thread_votes_by_time;
" | cqlsh
