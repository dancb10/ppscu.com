#!/usr/bin/env bash

echo "threads TABLE"
echo "
select * from threads.threads;
" | cqlsh

echo "threads_by_group TABLE"
echo "
select * from threads.threads_by_group;
" | cqlsh

echo "threads_by_group_create_date TABLE"
echo "
select * from threads.threads_by_group_create_date;
" | cqlsh

echo "thread_votes TABLE"
echo "
select * from threads.thread_votes;
" | cqlsh

echo "thread_votes_by_time TABLE"
echo "
select * from threads.thread_votes_by_time;
" | cqlsh
