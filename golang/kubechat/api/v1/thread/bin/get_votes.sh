#!/usr/bin/env bash

echo "thread_votes TABLE"
echo "
select * from threads.thread_votes;
" | cqlsh

echo "thread_votes_by_time TABLE"
echo "
select * from threads.thread_votes_by_time;
" | cqlsh
