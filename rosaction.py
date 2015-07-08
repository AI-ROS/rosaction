#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""ROS action client."""

import yaml
import roslib
import rosgraph
import rostopic
import actionlib

__author__ = "Anass Al-Wohoush"


def get_action_class(action):
    """Gets the corresponding ROS action class.

    Args:
        action: ROS action name.

    Returns:
        Action message class. None if not found.
    """
    goal_msg_type = rostopic.get_topic_type("{}/goal".format(action))[0]

    # Verify goal message was found.
    if not goal_msg_type:
        return None

    # Goal message name is the same as the action message name + 'Goal'.
    action_msg_type = goal_msg_type[:-4]

    return roslib.message.get_message_class(action_msg_type)


def get_goal_type(action):
    """Gets the corresponding ROS action goal type.

    Args:
        action: ROS action name.

    Returns:
        Tuple of (goal message type, goal topic name).
        (None, None) if not found.
    """
    return rostopic.get_topic_type("{}/goal".format(action))[:2]


def get_goal_class(action):
    """Gets the corresponding ROS action goal message class.

    Args:
        action: ROS action name.

    Returns:
        Tuple of (goal message class, goal topic name).
        (None, None) if not found.
    """
    return rostopic.get_topic_class("{}/goal".format(action))[:2]


def get_feedback_type(action):
    """Gets the corresponding ROS action feedback type.

    Args:
        action: ROS action name.

    Returns:
        Tuple of (feedback message type, feedback topic name).
        (None, None) if not found.
    """
    return rostopic.get_topic_type("{}/feedback".format(action))[:2]


def get_feedback_class(action):
    """Gets the corresponding ROS action feedback message class.

    Args:
        action: ROS action name.

    Returns:
        Tuple of (feedback message class, feedback topic name).
        (None, None) if not found.
    """
    return rostopic.get_topic_class("{}/feedback".format(action))[:2]


def get_result_type(action):
    """Gets the corresponding ROS action result type.

    Args:
        action: ROS action name.

    Returns:
        Tuple of (result message type, result topic name).
        (None, None) if not found.
    """
    return rostopic.get_topic_type("{}/result".format(action))[:2]


def get_result_class(action):
    """Gets the corresponding ROS action result message class.

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


def create_goal_from_yaml(action, msg):
    """Constructs goal from YAML encoded string.

    Args:
        action: ROS action name.
        msg: YAML encoded message.

    Returns:
        ROS action goal instance.
    """
    goal_cls, _ = get_goal_class(action)
    msg_dict = yaml.load(msg)
    return goal_cls(**msg_dict)


def create_action_client(action):
    """Creates corresponding ROS action client.

    Args:
        action: ROS action name.

    Returns:
        Corresponding actionlib.SimpleActionClient instance.
        None if action server not found.
    """
    action_cls = get_action_class(action)
    client = actionlib.SimpleActionClient(action, action_cls)
    return client


if __name__ == "__main__":
    for action in get_action_list():
        print(action)
