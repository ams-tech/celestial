Feature: rootfs_install

  Scenario Outline: update rootfs device node with expected fs format
    Given a rootfs file formatted with <expected_fs>
    And a target device node
    And we expect rootfs format <expected_fs>
    When we invoke celestial_rootfs_install
    Then the rootfs file is burned into the target device node

    Examples: Expected Filesystems
      | expected_fs   |
      | ext2          |
      | ext3          |
      | ext4          |


  Scenario Outline: faults when given an improperly formatted file
    Given a rootfs file formatted with <rootfs_format>
    And we expect rootfs format <expected_rootfs_format>
    When we invoke celestial_rootfs_install
    Then celestial_rootfs_install fails with ValueError

    Examples: Mismatched Filesystems
      # Since ext2 and ext3 formatted filesystems identify as ext2, we can't test for that fault
      | rootfs_format     | expected_rootfs_format    |
      | ext2              | ext4                      |
      | ext3              | ext4                      |
      | ext4              | ext2                      |
      | ext4              | ext3                      |
