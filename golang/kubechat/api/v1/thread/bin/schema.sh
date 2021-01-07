#!/usr/bin/env bash

echo "
CREATE KEYSPACE IF NOT EXISTS threads WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
" | cqlsh

echo "
CREATE TABLE IF NOT EXISTS threads.threads (
  thread_id UUID,
  group_id UUID,
  content text,
  create_date timestamp,
  labels list<text>,
  name text,
  plabels list <text>,
  summary text,
  update_date timestamp,
  PRIMARY KEY(thread_id, group_id));
" | cqlsh

echo "
CREATE TABLE IF NOT EXISTS threads.threads_by_group (
  group_id UUID,
  name text,
  create_date timestamp,
  labels list<text>,
  plabels list <text>,
  summary text,
  thread_id UUID,
  PRIMARY KEY(group_id, name)) WITH CLUSTERING ORDER BY (name ASC);
" | cqlsh

echo "
CREATE TABLE IF NOT EXISTS threads.threads_by_group_create_date (
  group_id UUID,
  day text,
  create_date timestamp,
  labels list<text>,
  name text,
  plabels list <text>,
  summary text,
  thread_id UUID,
  PRIMARY KEY((group_id, day), create_date)) WITH CLUSTERING ORDER BY (create_date DESC);
" | cqlsh

echo "
  CREATE TABLE IF NOT EXISTS threads.thread_votes(
    thread_id UUID,
    user_id UUID,
    day text,
    email text,
    first_name text,
    last_name text,
    vote_date timestamp,
    PRIMARY KEY ((thread_id), user_id));
" | cqlsh

echo "
  CREATE TABLE IF NOT EXISTS threads.thread_votes_by_time(
    thread_id UUID,
    day text,
    user_id UUID,
    email text,
    first_name text,
    last_name text,
    vote_date timestamp,
    PRIMARY KEY ((thread_id), day, user_id)) WITH CLUSTERING ORDER BY (day DESC);
" | cqlsh
