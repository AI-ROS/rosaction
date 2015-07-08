#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""ROS action client."""

import rostopic

__author__ = "Anass Al-Wohoush"


def get_goal_type(action):
    """Gets the ROS action goal type.

    Args:
        action: ROS action name.

    Returns:
        Tuple of (goal message type, goal topic name).
        (None, None) if not found.
    """
    return rostopic.get_topic_type("{}/goal".format(action))[:2]


def get_goal_class(action):
    """Gets the ROS action goal message class.

    Args:
        action: ROS action name.

    Returns:
        Tuple of (goal message class, goal topic name).
        (None, None) if not found.
    """
    return rostopic.get_topic_class("{}/goal".format(action))[:2]


def get_feedback_type(action):
    """Gets the ROS action feedback type.

    Args:
        action: ROS action name.

    Returns:
        Tuple of (feedback message type, feedback topic name).
        (None, None) if not found.
    """
    return rostopic.get_topic_type("{}/feedback".format(action))[:2]


def get_feedback_class(action):
    """Gets the ROS action feedback message class.

    Args:
        action: ROS action name.

    Returns:
        Tuple of (feedback message class, feedback topic name).
        (None, None) if not found.
    """
    return rostopic.get_topic_class("{}/feedback".format(action))[:2]


def get_result_type(action):
    """Gets the ROS action result type.

    Args:
        action: ROS action name.

    Returns:
        Tuple of (result message type, result topic name).
        (None, None) if not found.
    """
    return rostopic.get_topic_type("{}/result".format(action))[:2]


def get_result_class(action):
    """Gets the ROS action result message class.

    Args:
        action: ROS action name.

    Returns:
        Tuple of (result message class, result topic name).
        (None, None) if not found.
    """
    return rostopic.get_topic_class("{}/result".format(action))[:2]
