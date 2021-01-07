#!/usr/bin/env bash

echo "groups TABLE"
echo "
select * from groups.groups;
" | cqlsh

echo "groups_by_community TABLE"
echo "
select * from groups.groups_by_community;
" | cqlsh

echo "groups_by_community_create_date TABLE"
echo "
select * from groups.groups_by_community_create_date;
" | cqlsh

echo "groups_by_community_type TABLE"
echo "
select * from groups.groups_by_community_type;
" | cqlsh

echo "groups_by_community_visibility TABLE"
echo "
select * from groups.groups_by_community_visibility;
" | cqlsh
