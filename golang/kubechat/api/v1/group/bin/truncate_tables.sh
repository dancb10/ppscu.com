#!/usr/bin/env bash

echo "
TRUNCATE groups.groups;
" | cqlsh

echo "
TRUNCATE groups.groups_by_community;
" | cqlsh

echo "
TRUNCATE groups.groups_by_community_create_date;
" | cqlsh

echo "
TRUNCATE groups.groups_by_community_type;
" | cqlsh

echo "
TRUNCATE groups.groups_by_community_visibility;
" | cqlsh
