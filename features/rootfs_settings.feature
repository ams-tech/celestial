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
