#!/usr/bin/env bash

echo "
drop table threads.threads;
" | cqlsh

echo "
drop table threads.threads_by_group;
" | cqlsh

echo "
drop table threads.threads_by_group_create_date;
" | cqlsh

echo "
drop table threads.thread_votes;
" | cqlsh

echo "
drop table threads.thread_votes_by_time;
" | cqlsh
