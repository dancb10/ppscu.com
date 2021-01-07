#!/usr/bin/env bash

echo "
drop table groups.groups;
" | cqlsh

echo "
drop table groups.groups_by_community;
" | cqlsh

echo "
drop table groups.groups_by_community_create_date;
" | cqlsh

echo "
drop table groups.groups_by_community_type;
" | cqlsh

echo "
drop table groups.groups_by_community_visibility;
" | cqlsh
