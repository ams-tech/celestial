# Created by Adam at 6/1/2019
Feature: dual_rootfs_update
  Install a new rootfs and configure the system to boot with it using a
  dual-rootfs partition scheme

  Scenario Outline: install dual rootfs update
    Given a rootfs file formatted with <given_fs>
    And the sample cmdline file <sample_filename>
    And the boot rootfs device is set to <boot_device_node>
    And the rootfs device nodes are named <dev1> and <dev2>
    When we update the dual boot rootfs
    And we query the boot rootfs device
    Then the rootfs file is burned into <expected_device_node>
    And the reported boot rootfs device is <expected_device_node>

    Examples:
    | given_fs | sample_filename    | boot_device_node | dev1      | dev2      | expected_device_node |
    | ext3     | mmcblk0p1          | mmcblk0p1        | mmcblk0p1 | mmcblk0p2 | mmcblk0p2            |
    | ext4     | mmcblk0p2          | mmcblk0p2        | mmcblk0p1 | mmcblk0p2 | mmcblk0p1            |
    | ext4     | root_defined_first | mmcblk0p2        | mmcblk0p1 | mmcblk0p2 | mmcblk0p1            |
    | ext2     | root_defined_last  | mmcblk0p1        | mmcblk0p1 | mmcblk0p2 | mmcblk0p2            |

  Scenario: invalid boot device node fails
    Given a rootfs file formatted with ext3
    And the sample cmdline file mmcblk0p1
    And the boot rootfs device is set to mmcblk2p2
    And the rootfs device nodes are named mmcblk0p1 and mmcblk0p2
    When we update the dual boot rootfs
    Then dual_boot_update fails with ValueError

  Scenario: identical boot devices fails
    Given a rootfs file formatted with ext3
    And the sample cmdline file mmcblk0p1
    And the boot rootfs device is set to mmcblk0p1
    And the rootfs device nodes are named mmcblk0p1 and mmcblk0p1
    When we update the dual boot rootfs
    Then dual_boot_update fails with ValueError
