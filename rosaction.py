#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""ROS action client."""

import rosgraph
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


def get_action_list():
    """Gets list of registered ROS actions.

    Returns:
        List of ROS action names.
    """
    master = rosgraph.Master("/rosaction")

    # Get list of subscriptions from ROS master.
    _, subscriptions, _ = master.getSystemState()

    # Separate topic names from node names.
    registered_topics, _ = zip(*subscriptions)

    # All actions must have both '/goal' and '/cancel' topics.
    actions = [
        topic[:-5]  # Strip '/goal' from end of topic name.
        for topic in registered_topics
        if topic.endswith("/goal") and
        topic.replace("/goal", "/cancel") in registered_topics
    ]

    # Sort list for printing convenience.
    actions.sort()

    return actions


if __name__ == "__main__":
    for action in get_action_list():
        print(action)
