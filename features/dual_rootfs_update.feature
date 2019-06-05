# Created by Adam at 6/1/2019
Feature: dual_rootfs_update
  Install a new rootfs and configure the system to boot with it using a
  dual-rootfs partition scheme

  Scenario Outline: install dual rootfs update
    Given a rootfs file formatted with <given_fs>
    And the sample cmdline file <sample_filename>
    And the rootfs device nodes are <dev1> and <dev2>
    When we update the dual boot rootfs
    And we query the boot rootfs device
    Then the rootfs file is burned into <expected_device_node>
    And the reported boot rootfs device is <expected_device_node>

    Examples:
    | given_fs | sample_filename | dev1           | dev2           | expected_device_node  |
    | ext3     | mmcblk0p1       | /dev/mmcblk0p1 | /dev/mmcblk0p2 | /dev/mmcblk0p2        |
