# Created by Adam at 5/30/2019
Feature: rootfs_settings
  Determine and set the state of the rootfs partition

  Scenario Outline: get boot rootfs device
    Given the sample cmdline file <sample_filename>
    When we query the boot rootfs device
    Then the reported boot rootfs device is <expected_rootfs_device>

    Examples:
    | sample_filename     | expected_rootfs_device  |
    | mmcblk0p1           | /dev/mmcblk0p1          |
    | mmcblk0p2           | /dev/mmcblk0p2          |
    | root_defined_first  | /dev/mmcblk0p3          |
    | root_defined_last   | /dev/mmcblk2p4          |

  Scenario Outline: update boot rootfs device
    Given the sample cmdline file <sample_filename>
    And we want to boot with the rootfs at <new_rootfs_device>
    When we update the boot rootfs device in the cmdline file
    And we query the boot rootfs device
    Then the reported boot rootfs device is <new_rootfs_device>

    Examples:
    | sample_filename     | new_rootfs_device  |
    | mmcblk0p1           | /dev/mmcblk0p2     |
    | mmcblk0p2           | /dev/mmcblk0p1     |
    | root_defined_first  | /dev/mmcblk0p5     |
    | root_defined_last   | /dev/mmcblk1p3     |
    | mmcblk0p1           | /dev/mmcblk0p1     |
