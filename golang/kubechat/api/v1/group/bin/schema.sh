#!/usr/bin/env bash

echo "
CREATE KEYSPACE IF NOT EXISTS groups WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
" | cqlsh

echo "
CREATE TABLE IF NOT EXISTS groups.groups (
  group_id UUID,
  community_id UUID,
  create_date timestamp,
  description text,
  labels list<text>,
  name text,
  plabels list <text>,
  type text,
  update_date timestamp,
  visibility text,
  PRIMARY KEY(group_id, community_id));
" | cqlsh

echo "
CREATE TABLE IF NOT EXISTS groups.groups_by_community (
  community_id UUID,
  name text,
  create_date timestamp,
  description text,
  group_id UUID,
  labels list<text>,
  plabels list <text>,
  type text,
  visibility text,
  PRIMARY KEY(community_id, name)) WITH CLUSTERING ORDER BY (name ASC);
" | cqlsh

echo "
CREATE TABLE IF NOT EXISTS groups.groups_by_community_create_date (
  community_id UUID,
  day text,
  create_date timestamp,
  description text,
  group_id UUID,
  labels list<text>,
  name text,
  plabels list <text>,
  type text,
  visibility text,
  PRIMARY KEY((community_id, day), create_date)) WITH CLUSTERING ORDER BY (create_date DESC);
" | cqlsh

echo "
CREATE TABLE IF NOT EXISTS groups.groups_by_community_type (
  community_id UUID,
  type text,
  create_date timestamp,
  day text,
  description text,
  group_id UUID,
  labels list<text>,
  name text,
  plabels list <text>,
  visibility text,
  PRIMARY KEY((community_id, type), create_date)) WITH CLUSTERING ORDER BY (create_date DESC);
" | cqlsh

echo "
CREATE TABLE IF NOT EXISTS groups.groups_by_community_visibility (
  community_id UUID,
  visibility text,
  create_date timestamp,
  day text,
  description text,
  group_id UUID,
  labels list<text>,
  name text,
  plabels list <text>,
  type text,
  PRIMARY KEY((community_id, visibility), create_date)) WITH CLUSTERING ORDER BY (create_date DESC);
" | cqlsh
